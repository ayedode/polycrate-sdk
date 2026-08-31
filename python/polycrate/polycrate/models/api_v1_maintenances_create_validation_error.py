from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenances_create_actual_availability_error_component import (
        ApiV1MaintenancesCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_create_additional_recipients_error_component import (
        ApiV1MaintenancesCreateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_maintenances_create_affected_host_ids_error_component import (
        ApiV1MaintenancesCreateAffectedHostIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_create_affected_pop_ids_error_component import (
        ApiV1MaintenancesCreateAffectedPopIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_create_affected_volume_ids_error_component import (
        ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_create_annotations_error_component import (
        ApiV1MaintenancesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_maintenances_create_announcement_results_error_component import (
        ApiV1MaintenancesCreateAnnouncementResultsErrorComponent,
    )
    from ..models.api_v1_maintenances_create_announcement_sent_error_component import (
        ApiV1MaintenancesCreateAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_create_archived_at_error_component import (
        ApiV1MaintenancesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_maintenances_create_archived_by_error_component import (
        ApiV1MaintenancesCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_maintenances_create_archived_error_component import (
        ApiV1MaintenancesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_maintenances_create_archived_reason_error_component import (
        ApiV1MaintenancesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_maintenances_create_created_by_component_error_component import (
        ApiV1MaintenancesCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_maintenances_create_created_by_user_error_component import (
        ApiV1MaintenancesCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_create_criticality_error_component import (
        ApiV1MaintenancesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_maintenances_create_debug_mode_error_component import (
        ApiV1MaintenancesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_maintenances_create_discovery_enabled_error_component import (
        ApiV1MaintenancesCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_create_display_name_error_component import (
        ApiV1MaintenancesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_maintenances_create_draft_error_component import ApiV1MaintenancesCreateDraftErrorComponent
    from ..models.api_v1_maintenances_create_end_announcement_sent_error_component import (
        ApiV1MaintenancesCreateEndAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_create_end_error_component import ApiV1MaintenancesCreateEndErrorComponent
    from ..models.api_v1_maintenances_create_kind_error_component import ApiV1MaintenancesCreateKindErrorComponent
    from ..models.api_v1_maintenances_create_labels_error_component import ApiV1MaintenancesCreateLabelsErrorComponent
    from ..models.api_v1_maintenances_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_maintenances_create_managed_by_content_type_error_component import (
        ApiV1MaintenancesCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_maintenances_create_managed_by_object_id_error_component import (
        ApiV1MaintenancesCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_create_modified_by_user_error_component import (
        ApiV1MaintenancesCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_create_name_error_component import ApiV1MaintenancesCreateNameErrorComponent
    from ..models.api_v1_maintenances_create_non_field_errors_error_component import (
        ApiV1MaintenancesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_maintenances_create_notification_ended_sent_error_component import (
        ApiV1MaintenancesCreateNotificationEndedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_create_notification_scheduled_sent_error_component import (
        ApiV1MaintenancesCreateNotificationScheduledSentErrorComponent,
    )
    from ..models.api_v1_maintenances_create_notification_started_sent_error_component import (
        ApiV1MaintenancesCreateNotificationStartedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_create_organization_id_error_component import (
        ApiV1MaintenancesCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_maintenances_create_platform_dns_record_created_error_component import (
        ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_maintenances_create_platform_service_error_component import (
        ApiV1MaintenancesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_maintenances_create_project_id_error_component import (
        ApiV1MaintenancesCreateProjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_create_provider_entity_error_component import (
        ApiV1MaintenancesCreateProviderEntityErrorComponent,
    )
    from ..models.api_v1_maintenances_create_provider_error_component import (
        ApiV1MaintenancesCreateProviderErrorComponent,
    )
    from ..models.api_v1_maintenances_create_provider_id_error_component import (
        ApiV1MaintenancesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_maintenances_create_provider_reference_error_component import (
        ApiV1MaintenancesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_maintenances_create_reconciliation_enabled_error_component import (
        ApiV1MaintenancesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_create_reference_url_error_component import (
        ApiV1MaintenancesCreateReferenceUrlErrorComponent,
    )
    from ..models.api_v1_maintenances_create_scope_error_component import ApiV1MaintenancesCreateScopeErrorComponent
    from ..models.api_v1_maintenances_create_sla_availability_error_component import (
        ApiV1MaintenancesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_create_sla_target_error_component import (
        ApiV1MaintenancesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_create_sla_window_days_error_component import (
        ApiV1MaintenancesCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_create_slo_availability_error_component import (
        ApiV1MaintenancesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_create_slo_target_error_component import (
        ApiV1MaintenancesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_create_slo_window_days_error_component import (
        ApiV1MaintenancesCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_create_source_datasource_error_component import (
        ApiV1MaintenancesCreateSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_maintenances_create_source_item_id_error_component import (
        ApiV1MaintenancesCreateSourceItemIdErrorComponent,
    )
    from ..models.api_v1_maintenances_create_start_announcement_sent_error_component import (
        ApiV1MaintenancesCreateStartAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_create_start_error_component import ApiV1MaintenancesCreateStartErrorComponent
    from ..models.api_v1_maintenances_create_target_availability_error_component import (
        ApiV1MaintenancesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_create_timeline_error_component import (
        ApiV1MaintenancesCreateTimelineErrorComponent,
    )
    from ..models.api_v1_maintenances_create_workspace_id_error_component import (
        ApiV1MaintenancesCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenancesCreateValidationError")


@_attrs_define
class ApiV1MaintenancesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenancesCreateActualAvailabilityErrorComponent |
            ApiV1MaintenancesCreateAdditionalRecipientsErrorComponent | ApiV1MaintenancesCreateAffectedHostIdsErrorComponent
            | ApiV1MaintenancesCreateAffectedPopIdsErrorComponent | ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponent |
            ApiV1MaintenancesCreateAnnotationsErrorComponent | ApiV1MaintenancesCreateAnnouncementResultsErrorComponent |
            ApiV1MaintenancesCreateAnnouncementSentErrorComponent | ApiV1MaintenancesCreateArchivedAtErrorComponent |
            ApiV1MaintenancesCreateArchivedByErrorComponent | ApiV1MaintenancesCreateArchivedErrorComponent |
            ApiV1MaintenancesCreateArchivedReasonErrorComponent | ApiV1MaintenancesCreateCreatedByComponentErrorComponent |
            ApiV1MaintenancesCreateCreatedByUserErrorComponent | ApiV1MaintenancesCreateCriticalityErrorComponent |
            ApiV1MaintenancesCreateDebugModeErrorComponent | ApiV1MaintenancesCreateDiscoveryEnabledErrorComponent |
            ApiV1MaintenancesCreateDisplayNameErrorComponent | ApiV1MaintenancesCreateDraftErrorComponent |
            ApiV1MaintenancesCreateEndAnnouncementSentErrorComponent | ApiV1MaintenancesCreateEndErrorComponent |
            ApiV1MaintenancesCreateKindErrorComponent | ApiV1MaintenancesCreateLabelsErrorComponent |
            ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1MaintenancesCreateManagedByContentTypeErrorComponent |
            ApiV1MaintenancesCreateManagedByObjectIdErrorComponent | ApiV1MaintenancesCreateModifiedByUserErrorComponent |
            ApiV1MaintenancesCreateNameErrorComponent | ApiV1MaintenancesCreateNonFieldErrorsErrorComponent |
            ApiV1MaintenancesCreateNotificationEndedSentErrorComponent |
            ApiV1MaintenancesCreateNotificationScheduledSentErrorComponent |
            ApiV1MaintenancesCreateNotificationStartedSentErrorComponent |
            ApiV1MaintenancesCreateOrganizationIdErrorComponent |
            ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1MaintenancesCreatePlatformServiceErrorComponent | ApiV1MaintenancesCreateProjectIdErrorComponent |
            ApiV1MaintenancesCreateProviderEntityErrorComponent | ApiV1MaintenancesCreateProviderErrorComponent |
            ApiV1MaintenancesCreateProviderIdErrorComponent | ApiV1MaintenancesCreateProviderReferenceErrorComponent |
            ApiV1MaintenancesCreateReconciliationEnabledErrorComponent | ApiV1MaintenancesCreateReferenceUrlErrorComponent |
            ApiV1MaintenancesCreateScopeErrorComponent | ApiV1MaintenancesCreateSlaAvailabilityErrorComponent |
            ApiV1MaintenancesCreateSlaTargetErrorComponent | ApiV1MaintenancesCreateSlaWindowDaysErrorComponent |
            ApiV1MaintenancesCreateSloAvailabilityErrorComponent | ApiV1MaintenancesCreateSloTargetErrorComponent |
            ApiV1MaintenancesCreateSloWindowDaysErrorComponent | ApiV1MaintenancesCreateSourceDatasourceErrorComponent |
            ApiV1MaintenancesCreateSourceItemIdErrorComponent | ApiV1MaintenancesCreateStartAnnouncementSentErrorComponent |
            ApiV1MaintenancesCreateStartErrorComponent | ApiV1MaintenancesCreateTargetAvailabilityErrorComponent |
            ApiV1MaintenancesCreateTimelineErrorComponent | ApiV1MaintenancesCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenancesCreateActualAvailabilityErrorComponent
        | ApiV1MaintenancesCreateAdditionalRecipientsErrorComponent
        | ApiV1MaintenancesCreateAffectedHostIdsErrorComponent
        | ApiV1MaintenancesCreateAffectedPopIdsErrorComponent
        | ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponent
        | ApiV1MaintenancesCreateAnnotationsErrorComponent
        | ApiV1MaintenancesCreateAnnouncementResultsErrorComponent
        | ApiV1MaintenancesCreateAnnouncementSentErrorComponent
        | ApiV1MaintenancesCreateArchivedAtErrorComponent
        | ApiV1MaintenancesCreateArchivedByErrorComponent
        | ApiV1MaintenancesCreateArchivedErrorComponent
        | ApiV1MaintenancesCreateArchivedReasonErrorComponent
        | ApiV1MaintenancesCreateCreatedByComponentErrorComponent
        | ApiV1MaintenancesCreateCreatedByUserErrorComponent
        | ApiV1MaintenancesCreateCriticalityErrorComponent
        | ApiV1MaintenancesCreateDebugModeErrorComponent
        | ApiV1MaintenancesCreateDiscoveryEnabledErrorComponent
        | ApiV1MaintenancesCreateDisplayNameErrorComponent
        | ApiV1MaintenancesCreateDraftErrorComponent
        | ApiV1MaintenancesCreateEndAnnouncementSentErrorComponent
        | ApiV1MaintenancesCreateEndErrorComponent
        | ApiV1MaintenancesCreateKindErrorComponent
        | ApiV1MaintenancesCreateLabelsErrorComponent
        | ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1MaintenancesCreateManagedByContentTypeErrorComponent
        | ApiV1MaintenancesCreateManagedByObjectIdErrorComponent
        | ApiV1MaintenancesCreateModifiedByUserErrorComponent
        | ApiV1MaintenancesCreateNameErrorComponent
        | ApiV1MaintenancesCreateNonFieldErrorsErrorComponent
        | ApiV1MaintenancesCreateNotificationEndedSentErrorComponent
        | ApiV1MaintenancesCreateNotificationScheduledSentErrorComponent
        | ApiV1MaintenancesCreateNotificationStartedSentErrorComponent
        | ApiV1MaintenancesCreateOrganizationIdErrorComponent
        | ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1MaintenancesCreatePlatformServiceErrorComponent
        | ApiV1MaintenancesCreateProjectIdErrorComponent
        | ApiV1MaintenancesCreateProviderEntityErrorComponent
        | ApiV1MaintenancesCreateProviderErrorComponent
        | ApiV1MaintenancesCreateProviderIdErrorComponent
        | ApiV1MaintenancesCreateProviderReferenceErrorComponent
        | ApiV1MaintenancesCreateReconciliationEnabledErrorComponent
        | ApiV1MaintenancesCreateReferenceUrlErrorComponent
        | ApiV1MaintenancesCreateScopeErrorComponent
        | ApiV1MaintenancesCreateSlaAvailabilityErrorComponent
        | ApiV1MaintenancesCreateSlaTargetErrorComponent
        | ApiV1MaintenancesCreateSlaWindowDaysErrorComponent
        | ApiV1MaintenancesCreateSloAvailabilityErrorComponent
        | ApiV1MaintenancesCreateSloTargetErrorComponent
        | ApiV1MaintenancesCreateSloWindowDaysErrorComponent
        | ApiV1MaintenancesCreateSourceDatasourceErrorComponent
        | ApiV1MaintenancesCreateSourceItemIdErrorComponent
        | ApiV1MaintenancesCreateStartAnnouncementSentErrorComponent
        | ApiV1MaintenancesCreateStartErrorComponent
        | ApiV1MaintenancesCreateTargetAvailabilityErrorComponent
        | ApiV1MaintenancesCreateTimelineErrorComponent
        | ApiV1MaintenancesCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenances_create_actual_availability_error_component import (
            ApiV1MaintenancesCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_additional_recipients_error_component import (
            ApiV1MaintenancesCreateAdditionalRecipientsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_affected_host_ids_error_component import (
            ApiV1MaintenancesCreateAffectedHostIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_affected_pop_ids_error_component import (
            ApiV1MaintenancesCreateAffectedPopIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_affected_volume_ids_error_component import (
            ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_annotations_error_component import (
            ApiV1MaintenancesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_announcement_results_error_component import (
            ApiV1MaintenancesCreateAnnouncementResultsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_announcement_sent_error_component import (
            ApiV1MaintenancesCreateAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_archived_at_error_component import (
            ApiV1MaintenancesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_maintenances_create_archived_by_error_component import (
            ApiV1MaintenancesCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_maintenances_create_archived_error_component import (
            ApiV1MaintenancesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_maintenances_create_archived_reason_error_component import (
            ApiV1MaintenancesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_maintenances_create_created_by_component_error_component import (
            ApiV1MaintenancesCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_created_by_user_error_component import (
            ApiV1MaintenancesCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_maintenances_create_criticality_error_component import (
            ApiV1MaintenancesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_debug_mode_error_component import (
            ApiV1MaintenancesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_maintenances_create_discovery_enabled_error_component import (
            ApiV1MaintenancesCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_maintenances_create_display_name_error_component import (
            ApiV1MaintenancesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_maintenances_create_draft_error_component import ApiV1MaintenancesCreateDraftErrorComponent
        from ..models.api_v1_maintenances_create_end_announcement_sent_error_component import (
            ApiV1MaintenancesCreateEndAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_end_error_component import ApiV1MaintenancesCreateEndErrorComponent
        from ..models.api_v1_maintenances_create_kind_error_component import ApiV1MaintenancesCreateKindErrorComponent
        from ..models.api_v1_maintenances_create_labels_error_component import (
            ApiV1MaintenancesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_managed_by_content_type_error_component import (
            ApiV1MaintenancesCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_maintenances_create_managed_by_object_id_error_component import (
            ApiV1MaintenancesCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_modified_by_user_error_component import (
            ApiV1MaintenancesCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_maintenances_create_name_error_component import ApiV1MaintenancesCreateNameErrorComponent
        from ..models.api_v1_maintenances_create_non_field_errors_error_component import (
            ApiV1MaintenancesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_notification_ended_sent_error_component import (
            ApiV1MaintenancesCreateNotificationEndedSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesCreateNotificationScheduledSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_notification_started_sent_error_component import (
            ApiV1MaintenancesCreateNotificationStartedSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_organization_id_error_component import (
            ApiV1MaintenancesCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_platform_dns_record_created_error_component import (
            ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_maintenances_create_platform_service_error_component import (
            ApiV1MaintenancesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_maintenances_create_project_id_error_component import (
            ApiV1MaintenancesCreateProjectIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_provider_entity_error_component import (
            ApiV1MaintenancesCreateProviderEntityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_provider_error_component import (
            ApiV1MaintenancesCreateProviderErrorComponent,
        )
        from ..models.api_v1_maintenances_create_provider_id_error_component import (
            ApiV1MaintenancesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_provider_reference_error_component import (
            ApiV1MaintenancesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_maintenances_create_reconciliation_enabled_error_component import (
            ApiV1MaintenancesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_maintenances_create_reference_url_error_component import (
            ApiV1MaintenancesCreateReferenceUrlErrorComponent,
        )
        from ..models.api_v1_maintenances_create_scope_error_component import ApiV1MaintenancesCreateScopeErrorComponent
        from ..models.api_v1_maintenances_create_sla_availability_error_component import (
            ApiV1MaintenancesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_sla_target_error_component import (
            ApiV1MaintenancesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_maintenances_create_sla_window_days_error_component import (
            ApiV1MaintenancesCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_maintenances_create_slo_availability_error_component import (
            ApiV1MaintenancesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_slo_target_error_component import (
            ApiV1MaintenancesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_maintenances_create_slo_window_days_error_component import (
            ApiV1MaintenancesCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_maintenances_create_source_item_id_error_component import (
            ApiV1MaintenancesCreateSourceItemIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_start_announcement_sent_error_component import (
            ApiV1MaintenancesCreateStartAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_start_error_component import ApiV1MaintenancesCreateStartErrorComponent
        from ..models.api_v1_maintenances_create_target_availability_error_component import (
            ApiV1MaintenancesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_timeline_error_component import (
            ApiV1MaintenancesCreateTimelineErrorComponent,
        )
        from ..models.api_v1_maintenances_create_workspace_id_error_component import (
            ApiV1MaintenancesCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenancesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateAffectedHostIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateAffectedPopIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateSourceItemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateReferenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateStartAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateEndAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateAdditionalRecipientsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateAnnouncementResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateTimelineErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateNotificationScheduledSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateNotificationStartedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateNotificationEndedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesCreateProviderEntityErrorComponent):
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
        from ..models.api_v1_maintenances_create_actual_availability_error_component import (
            ApiV1MaintenancesCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_additional_recipients_error_component import (
            ApiV1MaintenancesCreateAdditionalRecipientsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_affected_host_ids_error_component import (
            ApiV1MaintenancesCreateAffectedHostIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_affected_pop_ids_error_component import (
            ApiV1MaintenancesCreateAffectedPopIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_affected_volume_ids_error_component import (
            ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_annotations_error_component import (
            ApiV1MaintenancesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_announcement_results_error_component import (
            ApiV1MaintenancesCreateAnnouncementResultsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_announcement_sent_error_component import (
            ApiV1MaintenancesCreateAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_archived_at_error_component import (
            ApiV1MaintenancesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_maintenances_create_archived_by_error_component import (
            ApiV1MaintenancesCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_maintenances_create_archived_error_component import (
            ApiV1MaintenancesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_maintenances_create_archived_reason_error_component import (
            ApiV1MaintenancesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_maintenances_create_created_by_component_error_component import (
            ApiV1MaintenancesCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_created_by_user_error_component import (
            ApiV1MaintenancesCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_maintenances_create_criticality_error_component import (
            ApiV1MaintenancesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_debug_mode_error_component import (
            ApiV1MaintenancesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_maintenances_create_discovery_enabled_error_component import (
            ApiV1MaintenancesCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_maintenances_create_display_name_error_component import (
            ApiV1MaintenancesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_maintenances_create_draft_error_component import ApiV1MaintenancesCreateDraftErrorComponent
        from ..models.api_v1_maintenances_create_end_announcement_sent_error_component import (
            ApiV1MaintenancesCreateEndAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_end_error_component import ApiV1MaintenancesCreateEndErrorComponent
        from ..models.api_v1_maintenances_create_kind_error_component import ApiV1MaintenancesCreateKindErrorComponent
        from ..models.api_v1_maintenances_create_labels_error_component import (
            ApiV1MaintenancesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_managed_by_content_type_error_component import (
            ApiV1MaintenancesCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_maintenances_create_managed_by_object_id_error_component import (
            ApiV1MaintenancesCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_modified_by_user_error_component import (
            ApiV1MaintenancesCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_maintenances_create_name_error_component import ApiV1MaintenancesCreateNameErrorComponent
        from ..models.api_v1_maintenances_create_non_field_errors_error_component import (
            ApiV1MaintenancesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_maintenances_create_notification_ended_sent_error_component import (
            ApiV1MaintenancesCreateNotificationEndedSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesCreateNotificationScheduledSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_notification_started_sent_error_component import (
            ApiV1MaintenancesCreateNotificationStartedSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_organization_id_error_component import (
            ApiV1MaintenancesCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_platform_dns_record_created_error_component import (
            ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_maintenances_create_platform_service_error_component import (
            ApiV1MaintenancesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_maintenances_create_project_id_error_component import (
            ApiV1MaintenancesCreateProjectIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_provider_entity_error_component import (
            ApiV1MaintenancesCreateProviderEntityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_provider_error_component import (
            ApiV1MaintenancesCreateProviderErrorComponent,
        )
        from ..models.api_v1_maintenances_create_provider_id_error_component import (
            ApiV1MaintenancesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_provider_reference_error_component import (
            ApiV1MaintenancesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_maintenances_create_reconciliation_enabled_error_component import (
            ApiV1MaintenancesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_maintenances_create_reference_url_error_component import (
            ApiV1MaintenancesCreateReferenceUrlErrorComponent,
        )
        from ..models.api_v1_maintenances_create_scope_error_component import ApiV1MaintenancesCreateScopeErrorComponent
        from ..models.api_v1_maintenances_create_sla_availability_error_component import (
            ApiV1MaintenancesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_sla_target_error_component import (
            ApiV1MaintenancesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_maintenances_create_sla_window_days_error_component import (
            ApiV1MaintenancesCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_maintenances_create_slo_availability_error_component import (
            ApiV1MaintenancesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_slo_target_error_component import (
            ApiV1MaintenancesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_maintenances_create_slo_window_days_error_component import (
            ApiV1MaintenancesCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_maintenances_create_source_datasource_error_component import (
            ApiV1MaintenancesCreateSourceDatasourceErrorComponent,
        )
        from ..models.api_v1_maintenances_create_source_item_id_error_component import (
            ApiV1MaintenancesCreateSourceItemIdErrorComponent,
        )
        from ..models.api_v1_maintenances_create_start_announcement_sent_error_component import (
            ApiV1MaintenancesCreateStartAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_create_start_error_component import ApiV1MaintenancesCreateStartErrorComponent
        from ..models.api_v1_maintenances_create_target_availability_error_component import (
            ApiV1MaintenancesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_create_timeline_error_component import (
            ApiV1MaintenancesCreateTimelineErrorComponent,
        )
        from ..models.api_v1_maintenances_create_workspace_id_error_component import (
            ApiV1MaintenancesCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenancesCreateActualAvailabilityErrorComponent
                | ApiV1MaintenancesCreateAdditionalRecipientsErrorComponent
                | ApiV1MaintenancesCreateAffectedHostIdsErrorComponent
                | ApiV1MaintenancesCreateAffectedPopIdsErrorComponent
                | ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponent
                | ApiV1MaintenancesCreateAnnotationsErrorComponent
                | ApiV1MaintenancesCreateAnnouncementResultsErrorComponent
                | ApiV1MaintenancesCreateAnnouncementSentErrorComponent
                | ApiV1MaintenancesCreateArchivedAtErrorComponent
                | ApiV1MaintenancesCreateArchivedByErrorComponent
                | ApiV1MaintenancesCreateArchivedErrorComponent
                | ApiV1MaintenancesCreateArchivedReasonErrorComponent
                | ApiV1MaintenancesCreateCreatedByComponentErrorComponent
                | ApiV1MaintenancesCreateCreatedByUserErrorComponent
                | ApiV1MaintenancesCreateCriticalityErrorComponent
                | ApiV1MaintenancesCreateDebugModeErrorComponent
                | ApiV1MaintenancesCreateDiscoveryEnabledErrorComponent
                | ApiV1MaintenancesCreateDisplayNameErrorComponent
                | ApiV1MaintenancesCreateDraftErrorComponent
                | ApiV1MaintenancesCreateEndAnnouncementSentErrorComponent
                | ApiV1MaintenancesCreateEndErrorComponent
                | ApiV1MaintenancesCreateKindErrorComponent
                | ApiV1MaintenancesCreateLabelsErrorComponent
                | ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1MaintenancesCreateManagedByContentTypeErrorComponent
                | ApiV1MaintenancesCreateManagedByObjectIdErrorComponent
                | ApiV1MaintenancesCreateModifiedByUserErrorComponent
                | ApiV1MaintenancesCreateNameErrorComponent
                | ApiV1MaintenancesCreateNonFieldErrorsErrorComponent
                | ApiV1MaintenancesCreateNotificationEndedSentErrorComponent
                | ApiV1MaintenancesCreateNotificationScheduledSentErrorComponent
                | ApiV1MaintenancesCreateNotificationStartedSentErrorComponent
                | ApiV1MaintenancesCreateOrganizationIdErrorComponent
                | ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1MaintenancesCreatePlatformServiceErrorComponent
                | ApiV1MaintenancesCreateProjectIdErrorComponent
                | ApiV1MaintenancesCreateProviderEntityErrorComponent
                | ApiV1MaintenancesCreateProviderErrorComponent
                | ApiV1MaintenancesCreateProviderIdErrorComponent
                | ApiV1MaintenancesCreateProviderReferenceErrorComponent
                | ApiV1MaintenancesCreateReconciliationEnabledErrorComponent
                | ApiV1MaintenancesCreateReferenceUrlErrorComponent
                | ApiV1MaintenancesCreateScopeErrorComponent
                | ApiV1MaintenancesCreateSlaAvailabilityErrorComponent
                | ApiV1MaintenancesCreateSlaTargetErrorComponent
                | ApiV1MaintenancesCreateSlaWindowDaysErrorComponent
                | ApiV1MaintenancesCreateSloAvailabilityErrorComponent
                | ApiV1MaintenancesCreateSloTargetErrorComponent
                | ApiV1MaintenancesCreateSloWindowDaysErrorComponent
                | ApiV1MaintenancesCreateSourceDatasourceErrorComponent
                | ApiV1MaintenancesCreateSourceItemIdErrorComponent
                | ApiV1MaintenancesCreateStartAnnouncementSentErrorComponent
                | ApiV1MaintenancesCreateStartErrorComponent
                | ApiV1MaintenancesCreateTargetAvailabilityErrorComponent
                | ApiV1MaintenancesCreateTimelineErrorComponent
                | ApiV1MaintenancesCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_0 = (
                        ApiV1MaintenancesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_1 = (
                        ApiV1MaintenancesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_2 = (
                        ApiV1MaintenancesCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_3 = (
                        ApiV1MaintenancesCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_4 = (
                        ApiV1MaintenancesCreateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_5 = (
                        ApiV1MaintenancesCreateAffectedHostIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_6 = (
                        ApiV1MaintenancesCreateAffectedVolumeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_7 = (
                        ApiV1MaintenancesCreateAffectedPopIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_8 = (
                        ApiV1MaintenancesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_9 = (
                        ApiV1MaintenancesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_10 = (
                        ApiV1MaintenancesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_11 = (
                        ApiV1MaintenancesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_12 = (
                        ApiV1MaintenancesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_13 = (
                        ApiV1MaintenancesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_14 = (
                        ApiV1MaintenancesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_15 = (
                        ApiV1MaintenancesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_16 = (
                        ApiV1MaintenancesCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_17 = (
                        ApiV1MaintenancesCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_18 = (
                        ApiV1MaintenancesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_19 = (
                        ApiV1MaintenancesCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_20 = (
                        ApiV1MaintenancesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_21 = (
                        ApiV1MaintenancesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_22 = (
                        ApiV1MaintenancesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_23 = (
                        ApiV1MaintenancesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_24 = (
                        ApiV1MaintenancesCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_25 = (
                        ApiV1MaintenancesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_26 = (
                        ApiV1MaintenancesCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_27 = (
                        ApiV1MaintenancesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_28 = (
                        ApiV1MaintenancesCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_29 = (
                        ApiV1MaintenancesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_30 = (
                        ApiV1MaintenancesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_31 = (
                        ApiV1MaintenancesCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_32 = (
                        ApiV1MaintenancesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_33 = (
                        ApiV1MaintenancesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_34 = (
                        ApiV1MaintenancesCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_35 = (
                        ApiV1MaintenancesCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_36 = (
                        ApiV1MaintenancesCreateStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_37 = (
                        ApiV1MaintenancesCreateEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_38 = (
                        ApiV1MaintenancesCreateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_39 = (
                        ApiV1MaintenancesCreateSourceItemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_40 = (
                        ApiV1MaintenancesCreateReferenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_41 = (
                        ApiV1MaintenancesCreateAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_42 = (
                        ApiV1MaintenancesCreateStartAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_43 = (
                        ApiV1MaintenancesCreateEndAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_44 = (
                        ApiV1MaintenancesCreateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_45 = (
                        ApiV1MaintenancesCreateAnnouncementResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_46 = (
                        ApiV1MaintenancesCreateTimelineErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_47 = (
                        ApiV1MaintenancesCreateNotificationScheduledSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_48 = (
                        ApiV1MaintenancesCreateNotificationStartedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_49 = (
                        ApiV1MaintenancesCreateNotificationEndedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_50 = (
                        ApiV1MaintenancesCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_51 = (
                        ApiV1MaintenancesCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_52 = (
                        ApiV1MaintenancesCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_53 = (
                        ApiV1MaintenancesCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_create_error_type_54 = (
                        ApiV1MaintenancesCreateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenances_create_error_type_55 = (
                    ApiV1MaintenancesCreateSourceDatasourceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenances_create_error_type_55

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenances_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenances_create_validation_error.additional_properties = d
        return api_v1_maintenances_create_validation_error

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
