from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenances_update_actual_availability_error_component import (
        ApiV1MaintenancesUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_update_additional_recipients_error_component import (
        ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_maintenances_update_affected_host_ids_error_component import (
        ApiV1MaintenancesUpdateAffectedHostIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_update_affected_pop_ids_error_component import (
        ApiV1MaintenancesUpdateAffectedPopIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_update_affected_volume_ids_error_component import (
        ApiV1MaintenancesUpdateAffectedVolumeIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_update_annotations_error_component import (
        ApiV1MaintenancesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_maintenances_update_announcement_results_error_component import (
        ApiV1MaintenancesUpdateAnnouncementResultsErrorComponent,
    )
    from ..models.api_v1_maintenances_update_announcement_sent_error_component import (
        ApiV1MaintenancesUpdateAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_update_archived_at_error_component import (
        ApiV1MaintenancesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_maintenances_update_archived_by_error_component import (
        ApiV1MaintenancesUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_maintenances_update_archived_error_component import (
        ApiV1MaintenancesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_maintenances_update_archived_reason_error_component import (
        ApiV1MaintenancesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_maintenances_update_created_by_component_error_component import (
        ApiV1MaintenancesUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_maintenances_update_created_by_user_error_component import (
        ApiV1MaintenancesUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_update_criticality_error_component import (
        ApiV1MaintenancesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_maintenances_update_debug_mode_error_component import (
        ApiV1MaintenancesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_maintenances_update_discovery_enabled_error_component import (
        ApiV1MaintenancesUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_update_display_name_error_component import (
        ApiV1MaintenancesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_maintenances_update_draft_error_component import ApiV1MaintenancesUpdateDraftErrorComponent
    from ..models.api_v1_maintenances_update_end_announcement_sent_error_component import (
        ApiV1MaintenancesUpdateEndAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_update_end_error_component import ApiV1MaintenancesUpdateEndErrorComponent
    from ..models.api_v1_maintenances_update_kind_error_component import ApiV1MaintenancesUpdateKindErrorComponent
    from ..models.api_v1_maintenances_update_labels_error_component import ApiV1MaintenancesUpdateLabelsErrorComponent
    from ..models.api_v1_maintenances_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1MaintenancesUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_maintenances_update_managed_by_content_type_error_component import (
        ApiV1MaintenancesUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_maintenances_update_managed_by_object_id_error_component import (
        ApiV1MaintenancesUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_update_modified_by_user_error_component import (
        ApiV1MaintenancesUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_update_name_error_component import ApiV1MaintenancesUpdateNameErrorComponent
    from ..models.api_v1_maintenances_update_non_field_errors_error_component import (
        ApiV1MaintenancesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_maintenances_update_notification_ended_sent_error_component import (
        ApiV1MaintenancesUpdateNotificationEndedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_update_notification_scheduled_sent_error_component import (
        ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponent,
    )
    from ..models.api_v1_maintenances_update_notification_started_sent_error_component import (
        ApiV1MaintenancesUpdateNotificationStartedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_update_organization_id_error_component import (
        ApiV1MaintenancesUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_maintenances_update_platform_dns_record_created_error_component import (
        ApiV1MaintenancesUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_maintenances_update_platform_service_error_component import (
        ApiV1MaintenancesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_maintenances_update_project_id_error_component import (
        ApiV1MaintenancesUpdateProjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_update_provider_entity_error_component import (
        ApiV1MaintenancesUpdateProviderEntityErrorComponent,
    )
    from ..models.api_v1_maintenances_update_provider_error_component import (
        ApiV1MaintenancesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_maintenances_update_provider_id_error_component import (
        ApiV1MaintenancesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_maintenances_update_provider_reference_error_component import (
        ApiV1MaintenancesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_maintenances_update_reconciliation_enabled_error_component import (
        ApiV1MaintenancesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_update_reference_url_error_component import (
        ApiV1MaintenancesUpdateReferenceUrlErrorComponent,
    )
    from ..models.api_v1_maintenances_update_scope_error_component import ApiV1MaintenancesUpdateScopeErrorComponent
    from ..models.api_v1_maintenances_update_sla_availability_error_component import (
        ApiV1MaintenancesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_update_sla_target_error_component import (
        ApiV1MaintenancesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_update_sla_window_days_error_component import (
        ApiV1MaintenancesUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_update_slo_availability_error_component import (
        ApiV1MaintenancesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_update_slo_target_error_component import (
        ApiV1MaintenancesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_update_slo_window_days_error_component import (
        ApiV1MaintenancesUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_update_source_datasource_error_component import (
        ApiV1MaintenancesUpdateSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_maintenances_update_source_item_id_error_component import (
        ApiV1MaintenancesUpdateSourceItemIdErrorComponent,
    )
    from ..models.api_v1_maintenances_update_start_announcement_sent_error_component import (
        ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_update_start_error_component import ApiV1MaintenancesUpdateStartErrorComponent
    from ..models.api_v1_maintenances_update_target_availability_error_component import (
        ApiV1MaintenancesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_update_timeline_error_component import (
        ApiV1MaintenancesUpdateTimelineErrorComponent,
    )
    from ..models.api_v1_maintenances_update_workspace_id_error_component import (
        ApiV1MaintenancesUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenancesUpdateValidationError")


@_attrs_define
class ApiV1MaintenancesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenancesUpdateActualAvailabilityErrorComponent |
            ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponent | ApiV1MaintenancesUpdateAffectedHostIdsErrorComponent
            | ApiV1MaintenancesUpdateAffectedPopIdsErrorComponent | ApiV1MaintenancesUpdateAffectedVolumeIdsErrorComponent |
            ApiV1MaintenancesUpdateAnnotationsErrorComponent | ApiV1MaintenancesUpdateAnnouncementResultsErrorComponent |
            ApiV1MaintenancesUpdateAnnouncementSentErrorComponent | ApiV1MaintenancesUpdateArchivedAtErrorComponent |
            ApiV1MaintenancesUpdateArchivedByErrorComponent | ApiV1MaintenancesUpdateArchivedErrorComponent |
            ApiV1MaintenancesUpdateArchivedReasonErrorComponent | ApiV1MaintenancesUpdateCreatedByComponentErrorComponent |
            ApiV1MaintenancesUpdateCreatedByUserErrorComponent | ApiV1MaintenancesUpdateCriticalityErrorComponent |
            ApiV1MaintenancesUpdateDebugModeErrorComponent | ApiV1MaintenancesUpdateDiscoveryEnabledErrorComponent |
            ApiV1MaintenancesUpdateDisplayNameErrorComponent | ApiV1MaintenancesUpdateDraftErrorComponent |
            ApiV1MaintenancesUpdateEndAnnouncementSentErrorComponent | ApiV1MaintenancesUpdateEndErrorComponent |
            ApiV1MaintenancesUpdateKindErrorComponent | ApiV1MaintenancesUpdateLabelsErrorComponent |
            ApiV1MaintenancesUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1MaintenancesUpdateManagedByContentTypeErrorComponent |
            ApiV1MaintenancesUpdateManagedByObjectIdErrorComponent | ApiV1MaintenancesUpdateModifiedByUserErrorComponent |
            ApiV1MaintenancesUpdateNameErrorComponent | ApiV1MaintenancesUpdateNonFieldErrorsErrorComponent |
            ApiV1MaintenancesUpdateNotificationEndedSentErrorComponent |
            ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponent |
            ApiV1MaintenancesUpdateNotificationStartedSentErrorComponent |
            ApiV1MaintenancesUpdateOrganizationIdErrorComponent |
            ApiV1MaintenancesUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1MaintenancesUpdatePlatformServiceErrorComponent | ApiV1MaintenancesUpdateProjectIdErrorComponent |
            ApiV1MaintenancesUpdateProviderEntityErrorComponent | ApiV1MaintenancesUpdateProviderErrorComponent |
            ApiV1MaintenancesUpdateProviderIdErrorComponent | ApiV1MaintenancesUpdateProviderReferenceErrorComponent |
            ApiV1MaintenancesUpdateReconciliationEnabledErrorComponent | ApiV1MaintenancesUpdateReferenceUrlErrorComponent |
            ApiV1MaintenancesUpdateScopeErrorComponent | ApiV1MaintenancesUpdateSlaAvailabilityErrorComponent |
            ApiV1MaintenancesUpdateSlaTargetErrorComponent | ApiV1MaintenancesUpdateSlaWindowDaysErrorComponent |
            ApiV1MaintenancesUpdateSloAvailabilityErrorComponent | ApiV1MaintenancesUpdateSloTargetErrorComponent |
            ApiV1MaintenancesUpdateSloWindowDaysErrorComponent | ApiV1MaintenancesUpdateSourceDatasourceErrorComponent |
            ApiV1MaintenancesUpdateSourceItemIdErrorComponent | ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponent |
            ApiV1MaintenancesUpdateStartErrorComponent | ApiV1MaintenancesUpdateTargetAvailabilityErrorComponent |
            ApiV1MaintenancesUpdateTimelineErrorComponent | ApiV1MaintenancesUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenancesUpdateActualAvailabilityErrorComponent
        | ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponent
        | ApiV1MaintenancesUpdateAffectedHostIdsErrorComponent
        | ApiV1MaintenancesUpdateAffectedPopIdsErrorComponent
        | ApiV1MaintenancesUpdateAffectedVolumeIdsErrorComponent
        | ApiV1MaintenancesUpdateAnnotationsErrorComponent
        | ApiV1MaintenancesUpdateAnnouncementResultsErrorComponent
        | ApiV1MaintenancesUpdateAnnouncementSentErrorComponent
        | ApiV1MaintenancesUpdateArchivedAtErrorComponent
        | ApiV1MaintenancesUpdateArchivedByErrorComponent
        | ApiV1MaintenancesUpdateArchivedErrorComponent
        | ApiV1MaintenancesUpdateArchivedReasonErrorComponent
        | ApiV1MaintenancesUpdateCreatedByComponentErrorComponent
        | ApiV1MaintenancesUpdateCreatedByUserErrorComponent
        | ApiV1MaintenancesUpdateCriticalityErrorComponent
        | ApiV1MaintenancesUpdateDebugModeErrorComponent
        | ApiV1MaintenancesUpdateDiscoveryEnabledErrorComponent
        | ApiV1MaintenancesUpdateDisplayNameErrorComponent
        | ApiV1MaintenancesUpdateDraftErrorComponent
        | ApiV1MaintenancesUpdateEndAnnouncementSentErrorComponent
        | ApiV1MaintenancesUpdateEndErrorComponent
        | ApiV1MaintenancesUpdateKindErrorComponent
        | ApiV1MaintenancesUpdateLabelsErrorComponent
        | ApiV1MaintenancesUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1MaintenancesUpdateManagedByContentTypeErrorComponent
        | ApiV1MaintenancesUpdateManagedByObjectIdErrorComponent
        | ApiV1MaintenancesUpdateModifiedByUserErrorComponent
        | ApiV1MaintenancesUpdateNameErrorComponent
        | ApiV1MaintenancesUpdateNonFieldErrorsErrorComponent
        | ApiV1MaintenancesUpdateNotificationEndedSentErrorComponent
        | ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponent
        | ApiV1MaintenancesUpdateNotificationStartedSentErrorComponent
        | ApiV1MaintenancesUpdateOrganizationIdErrorComponent
        | ApiV1MaintenancesUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1MaintenancesUpdatePlatformServiceErrorComponent
        | ApiV1MaintenancesUpdateProjectIdErrorComponent
        | ApiV1MaintenancesUpdateProviderEntityErrorComponent
        | ApiV1MaintenancesUpdateProviderErrorComponent
        | ApiV1MaintenancesUpdateProviderIdErrorComponent
        | ApiV1MaintenancesUpdateProviderReferenceErrorComponent
        | ApiV1MaintenancesUpdateReconciliationEnabledErrorComponent
        | ApiV1MaintenancesUpdateReferenceUrlErrorComponent
        | ApiV1MaintenancesUpdateScopeErrorComponent
        | ApiV1MaintenancesUpdateSlaAvailabilityErrorComponent
        | ApiV1MaintenancesUpdateSlaTargetErrorComponent
        | ApiV1MaintenancesUpdateSlaWindowDaysErrorComponent
        | ApiV1MaintenancesUpdateSloAvailabilityErrorComponent
        | ApiV1MaintenancesUpdateSloTargetErrorComponent
        | ApiV1MaintenancesUpdateSloWindowDaysErrorComponent
        | ApiV1MaintenancesUpdateSourceDatasourceErrorComponent
        | ApiV1MaintenancesUpdateSourceItemIdErrorComponent
        | ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponent
        | ApiV1MaintenancesUpdateStartErrorComponent
        | ApiV1MaintenancesUpdateTargetAvailabilityErrorComponent
        | ApiV1MaintenancesUpdateTimelineErrorComponent
        | ApiV1MaintenancesUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenances_update_actual_availability_error_component import (
            ApiV1MaintenancesUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_additional_recipients_error_component import (
            ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_affected_host_ids_error_component import (
            ApiV1MaintenancesUpdateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_affected_pop_ids_error_component import (
            ApiV1MaintenancesUpdateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_affected_volume_ids_error_component import (
            ApiV1MaintenancesUpdateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_annotations_error_component import (
            ApiV1MaintenancesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_announcement_results_error_component import (
            ApiV1MaintenancesUpdateAnnouncementResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_announcement_sent_error_component import (
            ApiV1MaintenancesUpdateAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_archived_at_error_component import (
            ApiV1MaintenancesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_archived_by_error_component import (
            ApiV1MaintenancesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_archived_error_component import (
            ApiV1MaintenancesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_archived_reason_error_component import (
            ApiV1MaintenancesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_created_by_component_error_component import (
            ApiV1MaintenancesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_created_by_user_error_component import (
            ApiV1MaintenancesUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_criticality_error_component import (
            ApiV1MaintenancesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_debug_mode_error_component import (
            ApiV1MaintenancesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_discovery_enabled_error_component import (
            ApiV1MaintenancesUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_display_name_error_component import (
            ApiV1MaintenancesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_draft_error_component import (
            ApiV1MaintenancesUpdateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_end_announcement_sent_error_component import (
            ApiV1MaintenancesUpdateEndAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_end_error_component import (
            ApiV1MaintenancesUpdateEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_kind_error_component import (
            ApiV1MaintenancesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_labels_error_component import (
            ApiV1MaintenancesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_managed_by_content_type_error_component import (
            ApiV1MaintenancesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_managed_by_object_id_error_component import (
            ApiV1MaintenancesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_modified_by_user_error_component import (
            ApiV1MaintenancesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_name_error_component import (
            ApiV1MaintenancesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_non_field_errors_error_component import (
            ApiV1MaintenancesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_notification_ended_sent_error_component import (
            ApiV1MaintenancesUpdateNotificationEndedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_notification_started_sent_error_component import (
            ApiV1MaintenancesUpdateNotificationStartedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_organization_id_error_component import (
            ApiV1MaintenancesUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_platform_dns_record_created_error_component import (
            ApiV1MaintenancesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_platform_service_error_component import (
            ApiV1MaintenancesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_project_id_error_component import (
            ApiV1MaintenancesUpdateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_provider_entity_error_component import (
            ApiV1MaintenancesUpdateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_provider_error_component import (
            ApiV1MaintenancesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_provider_id_error_component import (
            ApiV1MaintenancesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_provider_reference_error_component import (
            ApiV1MaintenancesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_reconciliation_enabled_error_component import (
            ApiV1MaintenancesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_reference_url_error_component import (
            ApiV1MaintenancesUpdateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_scope_error_component import (
            ApiV1MaintenancesUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_sla_availability_error_component import (
            ApiV1MaintenancesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_sla_target_error_component import (
            ApiV1MaintenancesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_sla_window_days_error_component import (
            ApiV1MaintenancesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_slo_availability_error_component import (
            ApiV1MaintenancesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_slo_target_error_component import (
            ApiV1MaintenancesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_slo_window_days_error_component import (
            ApiV1MaintenancesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_source_item_id_error_component import (
            ApiV1MaintenancesUpdateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_start_announcement_sent_error_component import (
            ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_start_error_component import (
            ApiV1MaintenancesUpdateStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_target_availability_error_component import (
            ApiV1MaintenancesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_timeline_error_component import (
            ApiV1MaintenancesUpdateTimelineErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_workspace_id_error_component import (
            ApiV1MaintenancesUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenancesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateAffectedHostIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateAffectedVolumeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateAffectedPopIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateSourceItemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateReferenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateEndAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateAnnouncementResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateTimelineErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateNotificationStartedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateNotificationEndedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesUpdateProviderEntityErrorComponent):
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
        from ..models.api_v1_maintenances_update_actual_availability_error_component import (
            ApiV1MaintenancesUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_additional_recipients_error_component import (
            ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_affected_host_ids_error_component import (
            ApiV1MaintenancesUpdateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_affected_pop_ids_error_component import (
            ApiV1MaintenancesUpdateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_affected_volume_ids_error_component import (
            ApiV1MaintenancesUpdateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_annotations_error_component import (
            ApiV1MaintenancesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_announcement_results_error_component import (
            ApiV1MaintenancesUpdateAnnouncementResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_announcement_sent_error_component import (
            ApiV1MaintenancesUpdateAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_archived_at_error_component import (
            ApiV1MaintenancesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_archived_by_error_component import (
            ApiV1MaintenancesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_archived_error_component import (
            ApiV1MaintenancesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_archived_reason_error_component import (
            ApiV1MaintenancesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_created_by_component_error_component import (
            ApiV1MaintenancesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_created_by_user_error_component import (
            ApiV1MaintenancesUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_criticality_error_component import (
            ApiV1MaintenancesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_debug_mode_error_component import (
            ApiV1MaintenancesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_discovery_enabled_error_component import (
            ApiV1MaintenancesUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_display_name_error_component import (
            ApiV1MaintenancesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_draft_error_component import (
            ApiV1MaintenancesUpdateDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_end_announcement_sent_error_component import (
            ApiV1MaintenancesUpdateEndAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_end_error_component import (
            ApiV1MaintenancesUpdateEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_kind_error_component import (
            ApiV1MaintenancesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_labels_error_component import (
            ApiV1MaintenancesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_managed_by_content_type_error_component import (
            ApiV1MaintenancesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_managed_by_object_id_error_component import (
            ApiV1MaintenancesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_modified_by_user_error_component import (
            ApiV1MaintenancesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_name_error_component import (
            ApiV1MaintenancesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_non_field_errors_error_component import (
            ApiV1MaintenancesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_notification_ended_sent_error_component import (
            ApiV1MaintenancesUpdateNotificationEndedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_notification_started_sent_error_component import (
            ApiV1MaintenancesUpdateNotificationStartedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_organization_id_error_component import (
            ApiV1MaintenancesUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_platform_dns_record_created_error_component import (
            ApiV1MaintenancesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_platform_service_error_component import (
            ApiV1MaintenancesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_project_id_error_component import (
            ApiV1MaintenancesUpdateProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_provider_entity_error_component import (
            ApiV1MaintenancesUpdateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_provider_error_component import (
            ApiV1MaintenancesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_provider_id_error_component import (
            ApiV1MaintenancesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_provider_reference_error_component import (
            ApiV1MaintenancesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_reconciliation_enabled_error_component import (
            ApiV1MaintenancesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_reference_url_error_component import (
            ApiV1MaintenancesUpdateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_scope_error_component import (
            ApiV1MaintenancesUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_sla_availability_error_component import (
            ApiV1MaintenancesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_sla_target_error_component import (
            ApiV1MaintenancesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_sla_window_days_error_component import (
            ApiV1MaintenancesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_slo_availability_error_component import (
            ApiV1MaintenancesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_slo_target_error_component import (
            ApiV1MaintenancesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_slo_window_days_error_component import (
            ApiV1MaintenancesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_source_datasource_error_component import (
            ApiV1MaintenancesUpdateSourceDatasourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_source_item_id_error_component import (
            ApiV1MaintenancesUpdateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_start_announcement_sent_error_component import (
            ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_start_error_component import (
            ApiV1MaintenancesUpdateStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_target_availability_error_component import (
            ApiV1MaintenancesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_timeline_error_component import (
            ApiV1MaintenancesUpdateTimelineErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenances_update_workspace_id_error_component import (
            ApiV1MaintenancesUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenancesUpdateActualAvailabilityErrorComponent
                | ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponent
                | ApiV1MaintenancesUpdateAffectedHostIdsErrorComponent
                | ApiV1MaintenancesUpdateAffectedPopIdsErrorComponent
                | ApiV1MaintenancesUpdateAffectedVolumeIdsErrorComponent
                | ApiV1MaintenancesUpdateAnnotationsErrorComponent
                | ApiV1MaintenancesUpdateAnnouncementResultsErrorComponent
                | ApiV1MaintenancesUpdateAnnouncementSentErrorComponent
                | ApiV1MaintenancesUpdateArchivedAtErrorComponent
                | ApiV1MaintenancesUpdateArchivedByErrorComponent
                | ApiV1MaintenancesUpdateArchivedErrorComponent
                | ApiV1MaintenancesUpdateArchivedReasonErrorComponent
                | ApiV1MaintenancesUpdateCreatedByComponentErrorComponent
                | ApiV1MaintenancesUpdateCreatedByUserErrorComponent
                | ApiV1MaintenancesUpdateCriticalityErrorComponent
                | ApiV1MaintenancesUpdateDebugModeErrorComponent
                | ApiV1MaintenancesUpdateDiscoveryEnabledErrorComponent
                | ApiV1MaintenancesUpdateDisplayNameErrorComponent
                | ApiV1MaintenancesUpdateDraftErrorComponent
                | ApiV1MaintenancesUpdateEndAnnouncementSentErrorComponent
                | ApiV1MaintenancesUpdateEndErrorComponent
                | ApiV1MaintenancesUpdateKindErrorComponent
                | ApiV1MaintenancesUpdateLabelsErrorComponent
                | ApiV1MaintenancesUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1MaintenancesUpdateManagedByContentTypeErrorComponent
                | ApiV1MaintenancesUpdateManagedByObjectIdErrorComponent
                | ApiV1MaintenancesUpdateModifiedByUserErrorComponent
                | ApiV1MaintenancesUpdateNameErrorComponent
                | ApiV1MaintenancesUpdateNonFieldErrorsErrorComponent
                | ApiV1MaintenancesUpdateNotificationEndedSentErrorComponent
                | ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponent
                | ApiV1MaintenancesUpdateNotificationStartedSentErrorComponent
                | ApiV1MaintenancesUpdateOrganizationIdErrorComponent
                | ApiV1MaintenancesUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1MaintenancesUpdatePlatformServiceErrorComponent
                | ApiV1MaintenancesUpdateProjectIdErrorComponent
                | ApiV1MaintenancesUpdateProviderEntityErrorComponent
                | ApiV1MaintenancesUpdateProviderErrorComponent
                | ApiV1MaintenancesUpdateProviderIdErrorComponent
                | ApiV1MaintenancesUpdateProviderReferenceErrorComponent
                | ApiV1MaintenancesUpdateReconciliationEnabledErrorComponent
                | ApiV1MaintenancesUpdateReferenceUrlErrorComponent
                | ApiV1MaintenancesUpdateScopeErrorComponent
                | ApiV1MaintenancesUpdateSlaAvailabilityErrorComponent
                | ApiV1MaintenancesUpdateSlaTargetErrorComponent
                | ApiV1MaintenancesUpdateSlaWindowDaysErrorComponent
                | ApiV1MaintenancesUpdateSloAvailabilityErrorComponent
                | ApiV1MaintenancesUpdateSloTargetErrorComponent
                | ApiV1MaintenancesUpdateSloWindowDaysErrorComponent
                | ApiV1MaintenancesUpdateSourceDatasourceErrorComponent
                | ApiV1MaintenancesUpdateSourceItemIdErrorComponent
                | ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponent
                | ApiV1MaintenancesUpdateStartErrorComponent
                | ApiV1MaintenancesUpdateTargetAvailabilityErrorComponent
                | ApiV1MaintenancesUpdateTimelineErrorComponent
                | ApiV1MaintenancesUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_0 = (
                        ApiV1MaintenancesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_1 = (
                        ApiV1MaintenancesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_2 = (
                        ApiV1MaintenancesUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_3 = (
                        ApiV1MaintenancesUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_4 = (
                        ApiV1MaintenancesUpdateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_5 = (
                        ApiV1MaintenancesUpdateAffectedHostIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_6 = (
                        ApiV1MaintenancesUpdateAffectedVolumeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_7 = (
                        ApiV1MaintenancesUpdateAffectedPopIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_8 = (
                        ApiV1MaintenancesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_9 = (
                        ApiV1MaintenancesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_10 = (
                        ApiV1MaintenancesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_11 = (
                        ApiV1MaintenancesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_12 = (
                        ApiV1MaintenancesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_13 = (
                        ApiV1MaintenancesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_14 = (
                        ApiV1MaintenancesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_15 = (
                        ApiV1MaintenancesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_16 = (
                        ApiV1MaintenancesUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_17 = (
                        ApiV1MaintenancesUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_18 = (
                        ApiV1MaintenancesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_19 = (
                        ApiV1MaintenancesUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_20 = (
                        ApiV1MaintenancesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_21 = (
                        ApiV1MaintenancesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_22 = (
                        ApiV1MaintenancesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_23 = (
                        ApiV1MaintenancesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_24 = (
                        ApiV1MaintenancesUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_25 = (
                        ApiV1MaintenancesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_26 = (
                        ApiV1MaintenancesUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_27 = (
                        ApiV1MaintenancesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_28 = (
                        ApiV1MaintenancesUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_29 = (
                        ApiV1MaintenancesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_30 = (
                        ApiV1MaintenancesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_31 = (
                        ApiV1MaintenancesUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_32 = (
                        ApiV1MaintenancesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_33 = (
                        ApiV1MaintenancesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_34 = (
                        ApiV1MaintenancesUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_35 = (
                        ApiV1MaintenancesUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_36 = (
                        ApiV1MaintenancesUpdateStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_37 = (
                        ApiV1MaintenancesUpdateEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_38 = (
                        ApiV1MaintenancesUpdateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_39 = (
                        ApiV1MaintenancesUpdateSourceItemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_40 = (
                        ApiV1MaintenancesUpdateReferenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_41 = (
                        ApiV1MaintenancesUpdateAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_42 = (
                        ApiV1MaintenancesUpdateStartAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_43 = (
                        ApiV1MaintenancesUpdateEndAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_44 = (
                        ApiV1MaintenancesUpdateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_45 = (
                        ApiV1MaintenancesUpdateAnnouncementResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_46 = (
                        ApiV1MaintenancesUpdateTimelineErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_47 = (
                        ApiV1MaintenancesUpdateNotificationScheduledSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_48 = (
                        ApiV1MaintenancesUpdateNotificationStartedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_49 = (
                        ApiV1MaintenancesUpdateNotificationEndedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_50 = (
                        ApiV1MaintenancesUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_51 = (
                        ApiV1MaintenancesUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_52 = (
                        ApiV1MaintenancesUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_53 = (
                        ApiV1MaintenancesUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_update_error_type_54 = (
                        ApiV1MaintenancesUpdateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenances_update_error_type_55 = (
                    ApiV1MaintenancesUpdateSourceDatasourceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenances_update_error_type_55

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenances_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenances_update_validation_error.additional_properties = d
        return api_v1_maintenances_update_validation_error

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
