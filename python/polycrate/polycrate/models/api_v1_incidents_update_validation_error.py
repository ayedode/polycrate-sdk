from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_incidents_update_actual_availability_error_component import (
        ApiV1IncidentsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_update_affected_host_ids_error_component import (
        ApiV1IncidentsUpdateAffectedHostIdsErrorComponent,
    )
    from ..models.api_v1_incidents_update_affected_pop_ids_error_component import (
        ApiV1IncidentsUpdateAffectedPopIdsErrorComponent,
    )
    from ..models.api_v1_incidents_update_affected_volume_ids_error_component import (
        ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponent,
    )
    from ..models.api_v1_incidents_update_annotations_error_component import (
        ApiV1IncidentsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_incidents_update_archived_at_error_component import (
        ApiV1IncidentsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_incidents_update_archived_by_error_component import (
        ApiV1IncidentsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_incidents_update_archived_error_component import ApiV1IncidentsUpdateArchivedErrorComponent
    from ..models.api_v1_incidents_update_archived_reason_error_component import (
        ApiV1IncidentsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_incidents_update_created_by_component_error_component import (
        ApiV1IncidentsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_incidents_update_created_by_user_error_component import (
        ApiV1IncidentsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_incidents_update_criticality_error_component import (
        ApiV1IncidentsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_incidents_update_debug_mode_error_component import ApiV1IncidentsUpdateDebugModeErrorComponent
    from ..models.api_v1_incidents_update_discovered_at_error_component import (
        ApiV1IncidentsUpdateDiscoveredAtErrorComponent,
    )
    from ..models.api_v1_incidents_update_discovery_enabled_error_component import (
        ApiV1IncidentsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_incidents_update_display_name_error_component import (
        ApiV1IncidentsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_incidents_update_downtime_ids_error_component import (
        ApiV1IncidentsUpdateDowntimeIdsErrorComponent,
    )
    from ..models.api_v1_incidents_update_kind_error_component import ApiV1IncidentsUpdateKindErrorComponent
    from ..models.api_v1_incidents_update_labels_error_component import ApiV1IncidentsUpdateLabelsErrorComponent
    from ..models.api_v1_incidents_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1IncidentsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_incidents_update_managed_by_content_type_error_component import (
        ApiV1IncidentsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_incidents_update_managed_by_object_id_error_component import (
        ApiV1IncidentsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_incidents_update_modified_by_user_error_component import (
        ApiV1IncidentsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_incidents_update_name_error_component import ApiV1IncidentsUpdateNameErrorComponent
    from ..models.api_v1_incidents_update_non_field_errors_error_component import (
        ApiV1IncidentsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_incidents_update_notification_closed_sent_error_component import (
        ApiV1IncidentsUpdateNotificationClosedSentErrorComponent,
    )
    from ..models.api_v1_incidents_update_notification_opened_sent_error_component import (
        ApiV1IncidentsUpdateNotificationOpenedSentErrorComponent,
    )
    from ..models.api_v1_incidents_update_occurred_at_error_component import (
        ApiV1IncidentsUpdateOccurredAtErrorComponent,
    )
    from ..models.api_v1_incidents_update_organization_id_error_component import (
        ApiV1IncidentsUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_incidents_update_platform_dns_record_created_error_component import (
        ApiV1IncidentsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_incidents_update_platform_service_error_component import (
        ApiV1IncidentsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_incidents_update_provider_entity_error_component import (
        ApiV1IncidentsUpdateProviderEntityErrorComponent,
    )
    from ..models.api_v1_incidents_update_provider_error_component import ApiV1IncidentsUpdateProviderErrorComponent
    from ..models.api_v1_incidents_update_provider_id_error_component import (
        ApiV1IncidentsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_incidents_update_provider_reference_error_component import (
        ApiV1IncidentsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_incidents_update_reconciliation_enabled_error_component import (
        ApiV1IncidentsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_incidents_update_reference_url_error_component import (
        ApiV1IncidentsUpdateReferenceUrlErrorComponent,
    )
    from ..models.api_v1_incidents_update_reporter_error_component import ApiV1IncidentsUpdateReporterErrorComponent
    from ..models.api_v1_incidents_update_resolved_at_error_component import (
        ApiV1IncidentsUpdateResolvedAtErrorComponent,
    )
    from ..models.api_v1_incidents_update_scope_error_component import ApiV1IncidentsUpdateScopeErrorComponent
    from ..models.api_v1_incidents_update_sla_availability_error_component import (
        ApiV1IncidentsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_update_sla_target_error_component import ApiV1IncidentsUpdateSlaTargetErrorComponent
    from ..models.api_v1_incidents_update_sla_window_days_error_component import (
        ApiV1IncidentsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_incidents_update_slo_availability_error_component import (
        ApiV1IncidentsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_update_slo_target_error_component import ApiV1IncidentsUpdateSloTargetErrorComponent
    from ..models.api_v1_incidents_update_slo_window_days_error_component import (
        ApiV1IncidentsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_incidents_update_source_datasource_error_component import (
        ApiV1IncidentsUpdateSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_incidents_update_source_item_id_error_component import (
        ApiV1IncidentsUpdateSourceItemIdErrorComponent,
    )
    from ..models.api_v1_incidents_update_status_error_component import ApiV1IncidentsUpdateStatusErrorComponent
    from ..models.api_v1_incidents_update_target_availability_error_component import (
        ApiV1IncidentsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_update_vulnerability_finding_ids_error_component import (
        ApiV1IncidentsUpdateVulnerabilityFindingIdsErrorComponent,
    )
    from ..models.api_v1_incidents_update_workspace_id_error_component import (
        ApiV1IncidentsUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IncidentsUpdateValidationError")


@_attrs_define
class ApiV1IncidentsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IncidentsUpdateActualAvailabilityErrorComponent |
            ApiV1IncidentsUpdateAffectedHostIdsErrorComponent | ApiV1IncidentsUpdateAffectedPopIdsErrorComponent |
            ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponent | ApiV1IncidentsUpdateAnnotationsErrorComponent |
            ApiV1IncidentsUpdateArchivedAtErrorComponent | ApiV1IncidentsUpdateArchivedByErrorComponent |
            ApiV1IncidentsUpdateArchivedErrorComponent | ApiV1IncidentsUpdateArchivedReasonErrorComponent |
            ApiV1IncidentsUpdateCreatedByComponentErrorComponent | ApiV1IncidentsUpdateCreatedByUserErrorComponent |
            ApiV1IncidentsUpdateCriticalityErrorComponent | ApiV1IncidentsUpdateDebugModeErrorComponent |
            ApiV1IncidentsUpdateDiscoveredAtErrorComponent | ApiV1IncidentsUpdateDiscoveryEnabledErrorComponent |
            ApiV1IncidentsUpdateDisplayNameErrorComponent | ApiV1IncidentsUpdateDowntimeIdsErrorComponent |
            ApiV1IncidentsUpdateKindErrorComponent | ApiV1IncidentsUpdateLabelsErrorComponent |
            ApiV1IncidentsUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1IncidentsUpdateManagedByContentTypeErrorComponent | ApiV1IncidentsUpdateManagedByObjectIdErrorComponent |
            ApiV1IncidentsUpdateModifiedByUserErrorComponent | ApiV1IncidentsUpdateNameErrorComponent |
            ApiV1IncidentsUpdateNonFieldErrorsErrorComponent | ApiV1IncidentsUpdateNotificationClosedSentErrorComponent |
            ApiV1IncidentsUpdateNotificationOpenedSentErrorComponent | ApiV1IncidentsUpdateOccurredAtErrorComponent |
            ApiV1IncidentsUpdateOrganizationIdErrorComponent | ApiV1IncidentsUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1IncidentsUpdatePlatformServiceErrorComponent | ApiV1IncidentsUpdateProviderEntityErrorComponent |
            ApiV1IncidentsUpdateProviderErrorComponent | ApiV1IncidentsUpdateProviderIdErrorComponent |
            ApiV1IncidentsUpdateProviderReferenceErrorComponent | ApiV1IncidentsUpdateReconciliationEnabledErrorComponent |
            ApiV1IncidentsUpdateReferenceUrlErrorComponent | ApiV1IncidentsUpdateReporterErrorComponent |
            ApiV1IncidentsUpdateResolvedAtErrorComponent | ApiV1IncidentsUpdateScopeErrorComponent |
            ApiV1IncidentsUpdateSlaAvailabilityErrorComponent | ApiV1IncidentsUpdateSlaTargetErrorComponent |
            ApiV1IncidentsUpdateSlaWindowDaysErrorComponent | ApiV1IncidentsUpdateSloAvailabilityErrorComponent |
            ApiV1IncidentsUpdateSloTargetErrorComponent | ApiV1IncidentsUpdateSloWindowDaysErrorComponent |
            ApiV1IncidentsUpdateSourceDatasourceErrorComponent | ApiV1IncidentsUpdateSourceItemIdErrorComponent |
            ApiV1IncidentsUpdateStatusErrorComponent | ApiV1IncidentsUpdateTargetAvailabilityErrorComponent |
            ApiV1IncidentsUpdateVulnerabilityFindingIdsErrorComponent | ApiV1IncidentsUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IncidentsUpdateActualAvailabilityErrorComponent
        | ApiV1IncidentsUpdateAffectedHostIdsErrorComponent
        | ApiV1IncidentsUpdateAffectedPopIdsErrorComponent
        | ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponent
        | ApiV1IncidentsUpdateAnnotationsErrorComponent
        | ApiV1IncidentsUpdateArchivedAtErrorComponent
        | ApiV1IncidentsUpdateArchivedByErrorComponent
        | ApiV1IncidentsUpdateArchivedErrorComponent
        | ApiV1IncidentsUpdateArchivedReasonErrorComponent
        | ApiV1IncidentsUpdateCreatedByComponentErrorComponent
        | ApiV1IncidentsUpdateCreatedByUserErrorComponent
        | ApiV1IncidentsUpdateCriticalityErrorComponent
        | ApiV1IncidentsUpdateDebugModeErrorComponent
        | ApiV1IncidentsUpdateDiscoveredAtErrorComponent
        | ApiV1IncidentsUpdateDiscoveryEnabledErrorComponent
        | ApiV1IncidentsUpdateDisplayNameErrorComponent
        | ApiV1IncidentsUpdateDowntimeIdsErrorComponent
        | ApiV1IncidentsUpdateKindErrorComponent
        | ApiV1IncidentsUpdateLabelsErrorComponent
        | ApiV1IncidentsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1IncidentsUpdateManagedByContentTypeErrorComponent
        | ApiV1IncidentsUpdateManagedByObjectIdErrorComponent
        | ApiV1IncidentsUpdateModifiedByUserErrorComponent
        | ApiV1IncidentsUpdateNameErrorComponent
        | ApiV1IncidentsUpdateNonFieldErrorsErrorComponent
        | ApiV1IncidentsUpdateNotificationClosedSentErrorComponent
        | ApiV1IncidentsUpdateNotificationOpenedSentErrorComponent
        | ApiV1IncidentsUpdateOccurredAtErrorComponent
        | ApiV1IncidentsUpdateOrganizationIdErrorComponent
        | ApiV1IncidentsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1IncidentsUpdatePlatformServiceErrorComponent
        | ApiV1IncidentsUpdateProviderEntityErrorComponent
        | ApiV1IncidentsUpdateProviderErrorComponent
        | ApiV1IncidentsUpdateProviderIdErrorComponent
        | ApiV1IncidentsUpdateProviderReferenceErrorComponent
        | ApiV1IncidentsUpdateReconciliationEnabledErrorComponent
        | ApiV1IncidentsUpdateReferenceUrlErrorComponent
        | ApiV1IncidentsUpdateReporterErrorComponent
        | ApiV1IncidentsUpdateResolvedAtErrorComponent
        | ApiV1IncidentsUpdateScopeErrorComponent
        | ApiV1IncidentsUpdateSlaAvailabilityErrorComponent
        | ApiV1IncidentsUpdateSlaTargetErrorComponent
        | ApiV1IncidentsUpdateSlaWindowDaysErrorComponent
        | ApiV1IncidentsUpdateSloAvailabilityErrorComponent
        | ApiV1IncidentsUpdateSloTargetErrorComponent
        | ApiV1IncidentsUpdateSloWindowDaysErrorComponent
        | ApiV1IncidentsUpdateSourceDatasourceErrorComponent
        | ApiV1IncidentsUpdateSourceItemIdErrorComponent
        | ApiV1IncidentsUpdateStatusErrorComponent
        | ApiV1IncidentsUpdateTargetAvailabilityErrorComponent
        | ApiV1IncidentsUpdateVulnerabilityFindingIdsErrorComponent
        | ApiV1IncidentsUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_incidents_update_actual_availability_error_component import (
            ApiV1IncidentsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_affected_host_ids_error_component import (
            ApiV1IncidentsUpdateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_affected_pop_ids_error_component import (
            ApiV1IncidentsUpdateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_affected_volume_ids_error_component import (
            ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_annotations_error_component import (
            ApiV1IncidentsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_archived_at_error_component import (
            ApiV1IncidentsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_archived_by_error_component import (
            ApiV1IncidentsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_archived_error_component import (
            ApiV1IncidentsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_archived_reason_error_component import (
            ApiV1IncidentsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_created_by_component_error_component import (
            ApiV1IncidentsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_created_by_user_error_component import (
            ApiV1IncidentsUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_criticality_error_component import (
            ApiV1IncidentsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_debug_mode_error_component import (
            ApiV1IncidentsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_discovered_at_error_component import (
            ApiV1IncidentsUpdateDiscoveredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_discovery_enabled_error_component import (
            ApiV1IncidentsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_display_name_error_component import (
            ApiV1IncidentsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_downtime_ids_error_component import (
            ApiV1IncidentsUpdateDowntimeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_kind_error_component import (
            ApiV1IncidentsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_labels_error_component import (
            ApiV1IncidentsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1IncidentsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_managed_by_content_type_error_component import (
            ApiV1IncidentsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_managed_by_object_id_error_component import (
            ApiV1IncidentsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_modified_by_user_error_component import (
            ApiV1IncidentsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_name_error_component import (
            ApiV1IncidentsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_non_field_errors_error_component import (
            ApiV1IncidentsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_notification_closed_sent_error_component import (
            ApiV1IncidentsUpdateNotificationClosedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_notification_opened_sent_error_component import (
            ApiV1IncidentsUpdateNotificationOpenedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_occurred_at_error_component import (
            ApiV1IncidentsUpdateOccurredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_organization_id_error_component import (
            ApiV1IncidentsUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_platform_dns_record_created_error_component import (
            ApiV1IncidentsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_platform_service_error_component import (
            ApiV1IncidentsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_provider_entity_error_component import (
            ApiV1IncidentsUpdateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_provider_error_component import (
            ApiV1IncidentsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_provider_id_error_component import (
            ApiV1IncidentsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_provider_reference_error_component import (
            ApiV1IncidentsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_reconciliation_enabled_error_component import (
            ApiV1IncidentsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_reference_url_error_component import (
            ApiV1IncidentsUpdateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_reporter_error_component import (
            ApiV1IncidentsUpdateReporterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_resolved_at_error_component import (
            ApiV1IncidentsUpdateResolvedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_scope_error_component import (
            ApiV1IncidentsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_sla_availability_error_component import (
            ApiV1IncidentsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_sla_target_error_component import (
            ApiV1IncidentsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_sla_window_days_error_component import (
            ApiV1IncidentsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_slo_availability_error_component import (
            ApiV1IncidentsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_slo_target_error_component import (
            ApiV1IncidentsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_slo_window_days_error_component import (
            ApiV1IncidentsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_source_item_id_error_component import (
            ApiV1IncidentsUpdateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_status_error_component import (
            ApiV1IncidentsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_target_availability_error_component import (
            ApiV1IncidentsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_vulnerability_finding_ids_error_component import (
            ApiV1IncidentsUpdateVulnerabilityFindingIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_workspace_id_error_component import (
            ApiV1IncidentsUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IncidentsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateDowntimeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateAffectedHostIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateAffectedPopIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateVulnerabilityFindingIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateOccurredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateDiscoveredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateResolvedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateReporterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateReferenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateSourceItemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateNotificationOpenedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateNotificationClosedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsUpdateProviderEntityErrorComponent):
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
        from ..models.api_v1_incidents_update_actual_availability_error_component import (
            ApiV1IncidentsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_affected_host_ids_error_component import (
            ApiV1IncidentsUpdateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_affected_pop_ids_error_component import (
            ApiV1IncidentsUpdateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_affected_volume_ids_error_component import (
            ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_annotations_error_component import (
            ApiV1IncidentsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_archived_at_error_component import (
            ApiV1IncidentsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_archived_by_error_component import (
            ApiV1IncidentsUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_archived_error_component import (
            ApiV1IncidentsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_archived_reason_error_component import (
            ApiV1IncidentsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_created_by_component_error_component import (
            ApiV1IncidentsUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_created_by_user_error_component import (
            ApiV1IncidentsUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_criticality_error_component import (
            ApiV1IncidentsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_debug_mode_error_component import (
            ApiV1IncidentsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_discovered_at_error_component import (
            ApiV1IncidentsUpdateDiscoveredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_discovery_enabled_error_component import (
            ApiV1IncidentsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_display_name_error_component import (
            ApiV1IncidentsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_downtime_ids_error_component import (
            ApiV1IncidentsUpdateDowntimeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_kind_error_component import (
            ApiV1IncidentsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_labels_error_component import (
            ApiV1IncidentsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1IncidentsUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_managed_by_content_type_error_component import (
            ApiV1IncidentsUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_managed_by_object_id_error_component import (
            ApiV1IncidentsUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_modified_by_user_error_component import (
            ApiV1IncidentsUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_name_error_component import (
            ApiV1IncidentsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_non_field_errors_error_component import (
            ApiV1IncidentsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_notification_closed_sent_error_component import (
            ApiV1IncidentsUpdateNotificationClosedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_notification_opened_sent_error_component import (
            ApiV1IncidentsUpdateNotificationOpenedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_occurred_at_error_component import (
            ApiV1IncidentsUpdateOccurredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_organization_id_error_component import (
            ApiV1IncidentsUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_platform_dns_record_created_error_component import (
            ApiV1IncidentsUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_platform_service_error_component import (
            ApiV1IncidentsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_provider_entity_error_component import (
            ApiV1IncidentsUpdateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_provider_error_component import (
            ApiV1IncidentsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_provider_id_error_component import (
            ApiV1IncidentsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_provider_reference_error_component import (
            ApiV1IncidentsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_reconciliation_enabled_error_component import (
            ApiV1IncidentsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_reference_url_error_component import (
            ApiV1IncidentsUpdateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_reporter_error_component import (
            ApiV1IncidentsUpdateReporterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_resolved_at_error_component import (
            ApiV1IncidentsUpdateResolvedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_scope_error_component import (
            ApiV1IncidentsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_sla_availability_error_component import (
            ApiV1IncidentsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_sla_target_error_component import (
            ApiV1IncidentsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_sla_window_days_error_component import (
            ApiV1IncidentsUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_slo_availability_error_component import (
            ApiV1IncidentsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_slo_target_error_component import (
            ApiV1IncidentsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_slo_window_days_error_component import (
            ApiV1IncidentsUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_source_datasource_error_component import (
            ApiV1IncidentsUpdateSourceDatasourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_source_item_id_error_component import (
            ApiV1IncidentsUpdateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_status_error_component import (
            ApiV1IncidentsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_target_availability_error_component import (
            ApiV1IncidentsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_vulnerability_finding_ids_error_component import (
            ApiV1IncidentsUpdateVulnerabilityFindingIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_update_workspace_id_error_component import (
            ApiV1IncidentsUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IncidentsUpdateActualAvailabilityErrorComponent
                | ApiV1IncidentsUpdateAffectedHostIdsErrorComponent
                | ApiV1IncidentsUpdateAffectedPopIdsErrorComponent
                | ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponent
                | ApiV1IncidentsUpdateAnnotationsErrorComponent
                | ApiV1IncidentsUpdateArchivedAtErrorComponent
                | ApiV1IncidentsUpdateArchivedByErrorComponent
                | ApiV1IncidentsUpdateArchivedErrorComponent
                | ApiV1IncidentsUpdateArchivedReasonErrorComponent
                | ApiV1IncidentsUpdateCreatedByComponentErrorComponent
                | ApiV1IncidentsUpdateCreatedByUserErrorComponent
                | ApiV1IncidentsUpdateCriticalityErrorComponent
                | ApiV1IncidentsUpdateDebugModeErrorComponent
                | ApiV1IncidentsUpdateDiscoveredAtErrorComponent
                | ApiV1IncidentsUpdateDiscoveryEnabledErrorComponent
                | ApiV1IncidentsUpdateDisplayNameErrorComponent
                | ApiV1IncidentsUpdateDowntimeIdsErrorComponent
                | ApiV1IncidentsUpdateKindErrorComponent
                | ApiV1IncidentsUpdateLabelsErrorComponent
                | ApiV1IncidentsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1IncidentsUpdateManagedByContentTypeErrorComponent
                | ApiV1IncidentsUpdateManagedByObjectIdErrorComponent
                | ApiV1IncidentsUpdateModifiedByUserErrorComponent
                | ApiV1IncidentsUpdateNameErrorComponent
                | ApiV1IncidentsUpdateNonFieldErrorsErrorComponent
                | ApiV1IncidentsUpdateNotificationClosedSentErrorComponent
                | ApiV1IncidentsUpdateNotificationOpenedSentErrorComponent
                | ApiV1IncidentsUpdateOccurredAtErrorComponent
                | ApiV1IncidentsUpdateOrganizationIdErrorComponent
                | ApiV1IncidentsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1IncidentsUpdatePlatformServiceErrorComponent
                | ApiV1IncidentsUpdateProviderEntityErrorComponent
                | ApiV1IncidentsUpdateProviderErrorComponent
                | ApiV1IncidentsUpdateProviderIdErrorComponent
                | ApiV1IncidentsUpdateProviderReferenceErrorComponent
                | ApiV1IncidentsUpdateReconciliationEnabledErrorComponent
                | ApiV1IncidentsUpdateReferenceUrlErrorComponent
                | ApiV1IncidentsUpdateReporterErrorComponent
                | ApiV1IncidentsUpdateResolvedAtErrorComponent
                | ApiV1IncidentsUpdateScopeErrorComponent
                | ApiV1IncidentsUpdateSlaAvailabilityErrorComponent
                | ApiV1IncidentsUpdateSlaTargetErrorComponent
                | ApiV1IncidentsUpdateSlaWindowDaysErrorComponent
                | ApiV1IncidentsUpdateSloAvailabilityErrorComponent
                | ApiV1IncidentsUpdateSloTargetErrorComponent
                | ApiV1IncidentsUpdateSloWindowDaysErrorComponent
                | ApiV1IncidentsUpdateSourceDatasourceErrorComponent
                | ApiV1IncidentsUpdateSourceItemIdErrorComponent
                | ApiV1IncidentsUpdateStatusErrorComponent
                | ApiV1IncidentsUpdateTargetAvailabilityErrorComponent
                | ApiV1IncidentsUpdateVulnerabilityFindingIdsErrorComponent
                | ApiV1IncidentsUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_0 = (
                        ApiV1IncidentsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_1 = (
                        ApiV1IncidentsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_2 = (
                        ApiV1IncidentsUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_3 = (
                        ApiV1IncidentsUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_4 = (
                        ApiV1IncidentsUpdateDowntimeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_5 = (
                        ApiV1IncidentsUpdateAffectedHostIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_6 = (
                        ApiV1IncidentsUpdateAffectedVolumeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_7 = (
                        ApiV1IncidentsUpdateAffectedPopIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_8 = (
                        ApiV1IncidentsUpdateVulnerabilityFindingIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_9 = (
                        ApiV1IncidentsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_10 = (
                        ApiV1IncidentsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_11 = (
                        ApiV1IncidentsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_12 = (
                        ApiV1IncidentsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_13 = (
                        ApiV1IncidentsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_14 = (
                        ApiV1IncidentsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_15 = (
                        ApiV1IncidentsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_16 = (
                        ApiV1IncidentsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_17 = (
                        ApiV1IncidentsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_18 = (
                        ApiV1IncidentsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_19 = (
                        ApiV1IncidentsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_20 = (
                        ApiV1IncidentsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_21 = (
                        ApiV1IncidentsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_22 = (
                        ApiV1IncidentsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_23 = (
                        ApiV1IncidentsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_24 = (
                        ApiV1IncidentsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_25 = (
                        ApiV1IncidentsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_26 = (
                        ApiV1IncidentsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_27 = (
                        ApiV1IncidentsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_28 = (
                        ApiV1IncidentsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_29 = (
                        ApiV1IncidentsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_30 = (
                        ApiV1IncidentsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_31 = (
                        ApiV1IncidentsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_32 = (
                        ApiV1IncidentsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_33 = (
                        ApiV1IncidentsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_34 = (
                        ApiV1IncidentsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_35 = (
                        ApiV1IncidentsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_36 = (
                        ApiV1IncidentsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_37 = (
                        ApiV1IncidentsUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_38 = (
                        ApiV1IncidentsUpdateOccurredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_39 = (
                        ApiV1IncidentsUpdateDiscoveredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_40 = (
                        ApiV1IncidentsUpdateResolvedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_41 = (
                        ApiV1IncidentsUpdateReporterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_42 = (
                        ApiV1IncidentsUpdateReferenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_43 = (
                        ApiV1IncidentsUpdateSourceItemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_44 = (
                        ApiV1IncidentsUpdateNotificationOpenedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_45 = (
                        ApiV1IncidentsUpdateNotificationClosedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_46 = (
                        ApiV1IncidentsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_47 = (
                        ApiV1IncidentsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_48 = (
                        ApiV1IncidentsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_49 = (
                        ApiV1IncidentsUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_update_error_type_50 = (
                        ApiV1IncidentsUpdateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_incidents_update_error_type_51 = (
                    ApiV1IncidentsUpdateSourceDatasourceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_incidents_update_error_type_51

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_incidents_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_incidents_update_validation_error.additional_properties = d
        return api_v1_incidents_update_validation_error

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
