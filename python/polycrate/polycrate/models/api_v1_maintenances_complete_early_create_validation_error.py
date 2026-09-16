from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenances_complete_early_create_actual_availability_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_additional_recipients_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_affected_host_ids_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_affected_pop_ids_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_affected_volume_ids_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateAffectedVolumeIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_annotations_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_announcement_results_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_announcement_sent_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_archived_at_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_archived_by_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_archived_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_archived_reason_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_created_by_component_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_created_by_user_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_criticality_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_debug_mode_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_discovery_enabled_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_display_name_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_draft_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateDraftErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_end_announcement_sent_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_end_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateEndErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_kind_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateKindErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_labels_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_managed_by_content_type_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_managed_by_object_id_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_modified_by_user_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_name_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateNameErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_non_field_errors_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_notification_ended_sent_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_notification_scheduled_sent_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateNotificationScheduledSentErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_notification_started_sent_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_organization_id_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_platform_dns_record_created_error_component import (
        ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_platform_service_error_component import (
        ApiV1MaintenancesCompleteEarlyCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_project_id_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_provider_entity_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateProviderEntityErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_provider_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_provider_id_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_provider_reference_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_reconciliation_enabled_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_reference_url_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_scope_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateScopeErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_sla_availability_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_sla_target_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_sla_window_days_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_slo_availability_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_slo_target_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_slo_window_days_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_source_datasource_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_source_item_id_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateSourceItemIdErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_start_announcement_sent_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_start_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateStartErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_target_availability_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_timeline_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponent,
    )
    from ..models.api_v1_maintenances_complete_early_create_workspace_id_error_component import (
        ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenancesCompleteEarlyCreateValidationError")


@_attrs_define
class ApiV1MaintenancesCompleteEarlyCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateAffectedVolumeIdsErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateAnnouncementSentErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateArchivedAtErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateArchivedReasonErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateDiscoveryEnabledErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateDisplayNameErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateDraftErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateEndErrorComponent | ApiV1MaintenancesCompleteEarlyCreateKindErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateManagedByContentTypeErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateManagedByObjectIdErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateNameErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateNonFieldErrorsErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateNotificationScheduledSentErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreatePlatformServiceErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateProviderEntityErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateProviderIdErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateScopeErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateSlaWindowDaysErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateSloAvailabilityErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateSloWindowDaysErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateSourceDatasourceErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateSourceItemIdErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateStartErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponent |
            ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateAffectedVolumeIdsErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateAnnouncementSentErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateArchivedAtErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateArchivedReasonErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateDiscoveryEnabledErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateDisplayNameErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateDraftErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateEndErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateKindErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateManagedByContentTypeErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateManagedByObjectIdErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateNameErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateNonFieldErrorsErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateNotificationScheduledSentErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreatePlatformServiceErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateProviderEntityErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateProviderIdErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateScopeErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateSlaWindowDaysErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateSloAvailabilityErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateSloWindowDaysErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateSourceDatasourceErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateSourceItemIdErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateStartErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponent
        | ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenances_complete_early_create_actual_availability_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_additional_recipients_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_affected_host_ids_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_affected_pop_ids_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_affected_volume_ids_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_annotations_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_announcement_results_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_announcement_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_archived_at_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_archived_by_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_archived_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_archived_reason_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_created_by_component_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_created_by_user_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_criticality_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_debug_mode_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_discovery_enabled_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_display_name_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_draft_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_end_announcement_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_end_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_kind_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_labels_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_managed_by_content_type_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_managed_by_object_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_modified_by_user_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_name_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_non_field_errors_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_notification_ended_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNotificationScheduledSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_notification_started_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_organization_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_platform_dns_record_created_error_component import (
            ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_platform_service_error_component import (
            ApiV1MaintenancesCompleteEarlyCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_project_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_provider_entity_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_provider_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_provider_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_provider_reference_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_reconciliation_enabled_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_reference_url_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_scope_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_sla_availability_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_sla_target_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_sla_window_days_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_slo_availability_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_slo_target_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_slo_window_days_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_source_item_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_start_announcement_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_start_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_target_availability_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_timeline_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_workspace_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateAffectedVolumeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateSourceItemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1MaintenancesCompleteEarlyCreateNotificationScheduledSentErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCompleteEarlyCreateProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_maintenances_complete_early_create_actual_availability_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_additional_recipients_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_affected_host_ids_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_affected_pop_ids_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_affected_volume_ids_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_annotations_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_announcement_results_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_announcement_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_archived_at_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_archived_by_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_archived_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_archived_reason_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_created_by_component_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_created_by_user_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_criticality_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_debug_mode_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_discovery_enabled_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_display_name_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_draft_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_end_announcement_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_end_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_kind_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_labels_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_managed_by_content_type_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_managed_by_object_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_modified_by_user_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_name_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_non_field_errors_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_notification_ended_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNotificationScheduledSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_notification_started_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_organization_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_platform_dns_record_created_error_component import (
            ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_platform_service_error_component import (
            ApiV1MaintenancesCompleteEarlyCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_project_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_provider_entity_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_provider_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_provider_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_provider_reference_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_reconciliation_enabled_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_reference_url_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_scope_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_sla_availability_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_sla_target_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_sla_window_days_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_slo_availability_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_slo_target_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_slo_window_days_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_source_datasource_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSourceDatasourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_source_item_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_start_announcement_sent_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_start_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_target_availability_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_timeline_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_complete_early_create_workspace_id_error_component import (
            ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateAffectedVolumeIdsErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateAnnouncementSentErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateArchivedAtErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateArchivedReasonErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateDiscoveryEnabledErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateDisplayNameErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateDraftErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateEndErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateKindErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateManagedByContentTypeErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateManagedByObjectIdErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateNameErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateNonFieldErrorsErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateNotificationScheduledSentErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreatePlatformServiceErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateProviderEntityErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateProviderIdErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateScopeErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateSlaWindowDaysErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateSloAvailabilityErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateSloWindowDaysErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateSourceDatasourceErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateSourceItemIdErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateStartErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponent
                | ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_0 = (
                        ApiV1MaintenancesCompleteEarlyCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_1 = (
                        ApiV1MaintenancesCompleteEarlyCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_2 = (
                        ApiV1MaintenancesCompleteEarlyCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_3 = (
                        ApiV1MaintenancesCompleteEarlyCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_4 = (
                        ApiV1MaintenancesCompleteEarlyCreateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_5 = (
                        ApiV1MaintenancesCompleteEarlyCreateAffectedHostIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_6 = (
                        ApiV1MaintenancesCompleteEarlyCreateAffectedVolumeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_7 = (
                        ApiV1MaintenancesCompleteEarlyCreateAffectedPopIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_8 = (
                        ApiV1MaintenancesCompleteEarlyCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_9 = (
                        ApiV1MaintenancesCompleteEarlyCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_10 = (
                        ApiV1MaintenancesCompleteEarlyCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_11 = (
                        ApiV1MaintenancesCompleteEarlyCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_12 = (
                        ApiV1MaintenancesCompleteEarlyCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_13 = (
                        ApiV1MaintenancesCompleteEarlyCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_14 = (
                        ApiV1MaintenancesCompleteEarlyCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_15 = (
                        ApiV1MaintenancesCompleteEarlyCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_16 = (
                        ApiV1MaintenancesCompleteEarlyCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_17 = (
                        ApiV1MaintenancesCompleteEarlyCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_18 = (
                        ApiV1MaintenancesCompleteEarlyCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_19 = (
                        ApiV1MaintenancesCompleteEarlyCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_20 = (
                        ApiV1MaintenancesCompleteEarlyCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_21 = (
                        ApiV1MaintenancesCompleteEarlyCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_22 = (
                        ApiV1MaintenancesCompleteEarlyCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_23 = (
                        ApiV1MaintenancesCompleteEarlyCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_24 = (
                        ApiV1MaintenancesCompleteEarlyCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_25 = (
                        ApiV1MaintenancesCompleteEarlyCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_26 = (
                        ApiV1MaintenancesCompleteEarlyCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_27 = (
                        ApiV1MaintenancesCompleteEarlyCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_28 = (
                        ApiV1MaintenancesCompleteEarlyCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_29 = (
                        ApiV1MaintenancesCompleteEarlyCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_30 = (
                        ApiV1MaintenancesCompleteEarlyCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_31 = (
                        ApiV1MaintenancesCompleteEarlyCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_32 = (
                        ApiV1MaintenancesCompleteEarlyCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_33 = (
                        ApiV1MaintenancesCompleteEarlyCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_34 = (
                        ApiV1MaintenancesCompleteEarlyCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_35 = (
                        ApiV1MaintenancesCompleteEarlyCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_36 = (
                        ApiV1MaintenancesCompleteEarlyCreateStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_37 = (
                        ApiV1MaintenancesCompleteEarlyCreateEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_38 = (
                        ApiV1MaintenancesCompleteEarlyCreateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_39 = (
                        ApiV1MaintenancesCompleteEarlyCreateSourceItemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_40 = (
                        ApiV1MaintenancesCompleteEarlyCreateReferenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_41 = (
                        ApiV1MaintenancesCompleteEarlyCreateAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_42 = (
                        ApiV1MaintenancesCompleteEarlyCreateStartAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_43 = (
                        ApiV1MaintenancesCompleteEarlyCreateEndAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_44 = (
                        ApiV1MaintenancesCompleteEarlyCreateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_45 = (
                        ApiV1MaintenancesCompleteEarlyCreateAnnouncementResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_46 = (
                        ApiV1MaintenancesCompleteEarlyCreateTimelineErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_47 = (
                        ApiV1MaintenancesCompleteEarlyCreateNotificationScheduledSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_48 = (
                        ApiV1MaintenancesCompleteEarlyCreateNotificationStartedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_49 = (
                        ApiV1MaintenancesCompleteEarlyCreateNotificationEndedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_50 = (
                        ApiV1MaintenancesCompleteEarlyCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_51 = (
                        ApiV1MaintenancesCompleteEarlyCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_52 = (
                        ApiV1MaintenancesCompleteEarlyCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_53 = (
                        ApiV1MaintenancesCompleteEarlyCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_complete_early_create_error_type_54 = (
                        ApiV1MaintenancesCompleteEarlyCreateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_complete_early_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenances_complete_early_create_error_type_55 = (
                    ApiV1MaintenancesCompleteEarlyCreateSourceDatasourceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenances_complete_early_create_error_type_55

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenances_complete_early_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenances_complete_early_create_validation_error.additional_properties = d
        return api_v1_maintenances_complete_early_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
