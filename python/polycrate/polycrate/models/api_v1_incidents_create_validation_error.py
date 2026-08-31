from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_incidents_create_actual_availability_error_component import (
        ApiV1IncidentsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_create_affected_host_ids_error_component import (
        ApiV1IncidentsCreateAffectedHostIdsErrorComponent,
    )
    from ..models.api_v1_incidents_create_affected_pop_ids_error_component import (
        ApiV1IncidentsCreateAffectedPopIdsErrorComponent,
    )
    from ..models.api_v1_incidents_create_affected_volume_ids_error_component import (
        ApiV1IncidentsCreateAffectedVolumeIdsErrorComponent,
    )
    from ..models.api_v1_incidents_create_annotations_error_component import (
        ApiV1IncidentsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_incidents_create_archived_at_error_component import (
        ApiV1IncidentsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_incidents_create_archived_by_error_component import (
        ApiV1IncidentsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_incidents_create_archived_error_component import ApiV1IncidentsCreateArchivedErrorComponent
    from ..models.api_v1_incidents_create_archived_reason_error_component import (
        ApiV1IncidentsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_incidents_create_created_by_component_error_component import (
        ApiV1IncidentsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_incidents_create_created_by_user_error_component import (
        ApiV1IncidentsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_incidents_create_criticality_error_component import (
        ApiV1IncidentsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_incidents_create_debug_mode_error_component import ApiV1IncidentsCreateDebugModeErrorComponent
    from ..models.api_v1_incidents_create_discovered_at_error_component import (
        ApiV1IncidentsCreateDiscoveredAtErrorComponent,
    )
    from ..models.api_v1_incidents_create_discovery_enabled_error_component import (
        ApiV1IncidentsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_incidents_create_display_name_error_component import (
        ApiV1IncidentsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_incidents_create_downtime_ids_error_component import (
        ApiV1IncidentsCreateDowntimeIdsErrorComponent,
    )
    from ..models.api_v1_incidents_create_kind_error_component import ApiV1IncidentsCreateKindErrorComponent
    from ..models.api_v1_incidents_create_labels_error_component import ApiV1IncidentsCreateLabelsErrorComponent
    from ..models.api_v1_incidents_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1IncidentsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_incidents_create_managed_by_content_type_error_component import (
        ApiV1IncidentsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_incidents_create_managed_by_object_id_error_component import (
        ApiV1IncidentsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_incidents_create_modified_by_user_error_component import (
        ApiV1IncidentsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_incidents_create_name_error_component import ApiV1IncidentsCreateNameErrorComponent
    from ..models.api_v1_incidents_create_non_field_errors_error_component import (
        ApiV1IncidentsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_incidents_create_notification_closed_sent_error_component import (
        ApiV1IncidentsCreateNotificationClosedSentErrorComponent,
    )
    from ..models.api_v1_incidents_create_notification_opened_sent_error_component import (
        ApiV1IncidentsCreateNotificationOpenedSentErrorComponent,
    )
    from ..models.api_v1_incidents_create_occurred_at_error_component import (
        ApiV1IncidentsCreateOccurredAtErrorComponent,
    )
    from ..models.api_v1_incidents_create_organization_id_error_component import (
        ApiV1IncidentsCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_incidents_create_platform_dns_record_created_error_component import (
        ApiV1IncidentsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_incidents_create_platform_service_error_component import (
        ApiV1IncidentsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_incidents_create_provider_entity_error_component import (
        ApiV1IncidentsCreateProviderEntityErrorComponent,
    )
    from ..models.api_v1_incidents_create_provider_error_component import ApiV1IncidentsCreateProviderErrorComponent
    from ..models.api_v1_incidents_create_provider_id_error_component import (
        ApiV1IncidentsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_incidents_create_provider_reference_error_component import (
        ApiV1IncidentsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_incidents_create_reconciliation_enabled_error_component import (
        ApiV1IncidentsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_incidents_create_reference_url_error_component import (
        ApiV1IncidentsCreateReferenceUrlErrorComponent,
    )
    from ..models.api_v1_incidents_create_reporter_error_component import ApiV1IncidentsCreateReporterErrorComponent
    from ..models.api_v1_incidents_create_resolved_at_error_component import (
        ApiV1IncidentsCreateResolvedAtErrorComponent,
    )
    from ..models.api_v1_incidents_create_scope_error_component import ApiV1IncidentsCreateScopeErrorComponent
    from ..models.api_v1_incidents_create_sla_availability_error_component import (
        ApiV1IncidentsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_create_sla_target_error_component import ApiV1IncidentsCreateSlaTargetErrorComponent
    from ..models.api_v1_incidents_create_sla_window_days_error_component import (
        ApiV1IncidentsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_incidents_create_slo_availability_error_component import (
        ApiV1IncidentsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_create_slo_target_error_component import ApiV1IncidentsCreateSloTargetErrorComponent
    from ..models.api_v1_incidents_create_slo_window_days_error_component import (
        ApiV1IncidentsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_incidents_create_source_datasource_error_component import (
        ApiV1IncidentsCreateSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_incidents_create_source_item_id_error_component import (
        ApiV1IncidentsCreateSourceItemIdErrorComponent,
    )
    from ..models.api_v1_incidents_create_status_error_component import ApiV1IncidentsCreateStatusErrorComponent
    from ..models.api_v1_incidents_create_target_availability_error_component import (
        ApiV1IncidentsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_create_vulnerability_finding_ids_error_component import (
        ApiV1IncidentsCreateVulnerabilityFindingIdsErrorComponent,
    )
    from ..models.api_v1_incidents_create_workspace_id_error_component import (
        ApiV1IncidentsCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IncidentsCreateValidationError")


@_attrs_define
class ApiV1IncidentsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IncidentsCreateActualAvailabilityErrorComponent |
            ApiV1IncidentsCreateAffectedHostIdsErrorComponent | ApiV1IncidentsCreateAffectedPopIdsErrorComponent |
            ApiV1IncidentsCreateAffectedVolumeIdsErrorComponent | ApiV1IncidentsCreateAnnotationsErrorComponent |
            ApiV1IncidentsCreateArchivedAtErrorComponent | ApiV1IncidentsCreateArchivedByErrorComponent |
            ApiV1IncidentsCreateArchivedErrorComponent | ApiV1IncidentsCreateArchivedReasonErrorComponent |
            ApiV1IncidentsCreateCreatedByComponentErrorComponent | ApiV1IncidentsCreateCreatedByUserErrorComponent |
            ApiV1IncidentsCreateCriticalityErrorComponent | ApiV1IncidentsCreateDebugModeErrorComponent |
            ApiV1IncidentsCreateDiscoveredAtErrorComponent | ApiV1IncidentsCreateDiscoveryEnabledErrorComponent |
            ApiV1IncidentsCreateDisplayNameErrorComponent | ApiV1IncidentsCreateDowntimeIdsErrorComponent |
            ApiV1IncidentsCreateKindErrorComponent | ApiV1IncidentsCreateLabelsErrorComponent |
            ApiV1IncidentsCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1IncidentsCreateManagedByContentTypeErrorComponent | ApiV1IncidentsCreateManagedByObjectIdErrorComponent |
            ApiV1IncidentsCreateModifiedByUserErrorComponent | ApiV1IncidentsCreateNameErrorComponent |
            ApiV1IncidentsCreateNonFieldErrorsErrorComponent | ApiV1IncidentsCreateNotificationClosedSentErrorComponent |
            ApiV1IncidentsCreateNotificationOpenedSentErrorComponent | ApiV1IncidentsCreateOccurredAtErrorComponent |
            ApiV1IncidentsCreateOrganizationIdErrorComponent | ApiV1IncidentsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1IncidentsCreatePlatformServiceErrorComponent | ApiV1IncidentsCreateProviderEntityErrorComponent |
            ApiV1IncidentsCreateProviderErrorComponent | ApiV1IncidentsCreateProviderIdErrorComponent |
            ApiV1IncidentsCreateProviderReferenceErrorComponent | ApiV1IncidentsCreateReconciliationEnabledErrorComponent |
            ApiV1IncidentsCreateReferenceUrlErrorComponent | ApiV1IncidentsCreateReporterErrorComponent |
            ApiV1IncidentsCreateResolvedAtErrorComponent | ApiV1IncidentsCreateScopeErrorComponent |
            ApiV1IncidentsCreateSlaAvailabilityErrorComponent | ApiV1IncidentsCreateSlaTargetErrorComponent |
            ApiV1IncidentsCreateSlaWindowDaysErrorComponent | ApiV1IncidentsCreateSloAvailabilityErrorComponent |
            ApiV1IncidentsCreateSloTargetErrorComponent | ApiV1IncidentsCreateSloWindowDaysErrorComponent |
            ApiV1IncidentsCreateSourceDatasourceErrorComponent | ApiV1IncidentsCreateSourceItemIdErrorComponent |
            ApiV1IncidentsCreateStatusErrorComponent | ApiV1IncidentsCreateTargetAvailabilityErrorComponent |
            ApiV1IncidentsCreateVulnerabilityFindingIdsErrorComponent | ApiV1IncidentsCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IncidentsCreateActualAvailabilityErrorComponent
        | ApiV1IncidentsCreateAffectedHostIdsErrorComponent
        | ApiV1IncidentsCreateAffectedPopIdsErrorComponent
        | ApiV1IncidentsCreateAffectedVolumeIdsErrorComponent
        | ApiV1IncidentsCreateAnnotationsErrorComponent
        | ApiV1IncidentsCreateArchivedAtErrorComponent
        | ApiV1IncidentsCreateArchivedByErrorComponent
        | ApiV1IncidentsCreateArchivedErrorComponent
        | ApiV1IncidentsCreateArchivedReasonErrorComponent
        | ApiV1IncidentsCreateCreatedByComponentErrorComponent
        | ApiV1IncidentsCreateCreatedByUserErrorComponent
        | ApiV1IncidentsCreateCriticalityErrorComponent
        | ApiV1IncidentsCreateDebugModeErrorComponent
        | ApiV1IncidentsCreateDiscoveredAtErrorComponent
        | ApiV1IncidentsCreateDiscoveryEnabledErrorComponent
        | ApiV1IncidentsCreateDisplayNameErrorComponent
        | ApiV1IncidentsCreateDowntimeIdsErrorComponent
        | ApiV1IncidentsCreateKindErrorComponent
        | ApiV1IncidentsCreateLabelsErrorComponent
        | ApiV1IncidentsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1IncidentsCreateManagedByContentTypeErrorComponent
        | ApiV1IncidentsCreateManagedByObjectIdErrorComponent
        | ApiV1IncidentsCreateModifiedByUserErrorComponent
        | ApiV1IncidentsCreateNameErrorComponent
        | ApiV1IncidentsCreateNonFieldErrorsErrorComponent
        | ApiV1IncidentsCreateNotificationClosedSentErrorComponent
        | ApiV1IncidentsCreateNotificationOpenedSentErrorComponent
        | ApiV1IncidentsCreateOccurredAtErrorComponent
        | ApiV1IncidentsCreateOrganizationIdErrorComponent
        | ApiV1IncidentsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1IncidentsCreatePlatformServiceErrorComponent
        | ApiV1IncidentsCreateProviderEntityErrorComponent
        | ApiV1IncidentsCreateProviderErrorComponent
        | ApiV1IncidentsCreateProviderIdErrorComponent
        | ApiV1IncidentsCreateProviderReferenceErrorComponent
        | ApiV1IncidentsCreateReconciliationEnabledErrorComponent
        | ApiV1IncidentsCreateReferenceUrlErrorComponent
        | ApiV1IncidentsCreateReporterErrorComponent
        | ApiV1IncidentsCreateResolvedAtErrorComponent
        | ApiV1IncidentsCreateScopeErrorComponent
        | ApiV1IncidentsCreateSlaAvailabilityErrorComponent
        | ApiV1IncidentsCreateSlaTargetErrorComponent
        | ApiV1IncidentsCreateSlaWindowDaysErrorComponent
        | ApiV1IncidentsCreateSloAvailabilityErrorComponent
        | ApiV1IncidentsCreateSloTargetErrorComponent
        | ApiV1IncidentsCreateSloWindowDaysErrorComponent
        | ApiV1IncidentsCreateSourceDatasourceErrorComponent
        | ApiV1IncidentsCreateSourceItemIdErrorComponent
        | ApiV1IncidentsCreateStatusErrorComponent
        | ApiV1IncidentsCreateTargetAvailabilityErrorComponent
        | ApiV1IncidentsCreateVulnerabilityFindingIdsErrorComponent
        | ApiV1IncidentsCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_incidents_create_actual_availability_error_component import (
            ApiV1IncidentsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_incidents_create_affected_host_ids_error_component import (
            ApiV1IncidentsCreateAffectedHostIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_affected_pop_ids_error_component import (
            ApiV1IncidentsCreateAffectedPopIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_affected_volume_ids_error_component import (
            ApiV1IncidentsCreateAffectedVolumeIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_annotations_error_component import (
            ApiV1IncidentsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_incidents_create_archived_at_error_component import (
            ApiV1IncidentsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_incidents_create_archived_by_error_component import (
            ApiV1IncidentsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_incidents_create_archived_error_component import ApiV1IncidentsCreateArchivedErrorComponent
        from ..models.api_v1_incidents_create_archived_reason_error_component import (
            ApiV1IncidentsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_incidents_create_created_by_component_error_component import (
            ApiV1IncidentsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_incidents_create_created_by_user_error_component import (
            ApiV1IncidentsCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_incidents_create_criticality_error_component import (
            ApiV1IncidentsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_incidents_create_debug_mode_error_component import (
            ApiV1IncidentsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_incidents_create_discovered_at_error_component import (
            ApiV1IncidentsCreateDiscoveredAtErrorComponent,
        )
        from ..models.api_v1_incidents_create_discovery_enabled_error_component import (
            ApiV1IncidentsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_incidents_create_display_name_error_component import (
            ApiV1IncidentsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_incidents_create_downtime_ids_error_component import (
            ApiV1IncidentsCreateDowntimeIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_kind_error_component import ApiV1IncidentsCreateKindErrorComponent
        from ..models.api_v1_incidents_create_labels_error_component import ApiV1IncidentsCreateLabelsErrorComponent
        from ..models.api_v1_incidents_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1IncidentsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_incidents_create_managed_by_content_type_error_component import (
            ApiV1IncidentsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_incidents_create_managed_by_object_id_error_component import (
            ApiV1IncidentsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_incidents_create_modified_by_user_error_component import (
            ApiV1IncidentsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_incidents_create_name_error_component import ApiV1IncidentsCreateNameErrorComponent
        from ..models.api_v1_incidents_create_non_field_errors_error_component import (
            ApiV1IncidentsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_incidents_create_notification_closed_sent_error_component import (
            ApiV1IncidentsCreateNotificationClosedSentErrorComponent,
        )
        from ..models.api_v1_incidents_create_notification_opened_sent_error_component import (
            ApiV1IncidentsCreateNotificationOpenedSentErrorComponent,
        )
        from ..models.api_v1_incidents_create_occurred_at_error_component import (
            ApiV1IncidentsCreateOccurredAtErrorComponent,
        )
        from ..models.api_v1_incidents_create_organization_id_error_component import (
            ApiV1IncidentsCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_incidents_create_platform_dns_record_created_error_component import (
            ApiV1IncidentsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_incidents_create_platform_service_error_component import (
            ApiV1IncidentsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_incidents_create_provider_entity_error_component import (
            ApiV1IncidentsCreateProviderEntityErrorComponent,
        )
        from ..models.api_v1_incidents_create_provider_error_component import ApiV1IncidentsCreateProviderErrorComponent
        from ..models.api_v1_incidents_create_provider_id_error_component import (
            ApiV1IncidentsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_incidents_create_provider_reference_error_component import (
            ApiV1IncidentsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_incidents_create_reconciliation_enabled_error_component import (
            ApiV1IncidentsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_incidents_create_reference_url_error_component import (
            ApiV1IncidentsCreateReferenceUrlErrorComponent,
        )
        from ..models.api_v1_incidents_create_reporter_error_component import ApiV1IncidentsCreateReporterErrorComponent
        from ..models.api_v1_incidents_create_resolved_at_error_component import (
            ApiV1IncidentsCreateResolvedAtErrorComponent,
        )
        from ..models.api_v1_incidents_create_scope_error_component import ApiV1IncidentsCreateScopeErrorComponent
        from ..models.api_v1_incidents_create_sla_availability_error_component import (
            ApiV1IncidentsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_incidents_create_sla_target_error_component import (
            ApiV1IncidentsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_incidents_create_sla_window_days_error_component import (
            ApiV1IncidentsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_incidents_create_slo_availability_error_component import (
            ApiV1IncidentsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_incidents_create_slo_target_error_component import (
            ApiV1IncidentsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_incidents_create_slo_window_days_error_component import (
            ApiV1IncidentsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_incidents_create_source_item_id_error_component import (
            ApiV1IncidentsCreateSourceItemIdErrorComponent,
        )
        from ..models.api_v1_incidents_create_status_error_component import ApiV1IncidentsCreateStatusErrorComponent
        from ..models.api_v1_incidents_create_target_availability_error_component import (
            ApiV1IncidentsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_incidents_create_vulnerability_finding_ids_error_component import (
            ApiV1IncidentsCreateVulnerabilityFindingIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_workspace_id_error_component import (
            ApiV1IncidentsCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IncidentsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateDowntimeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateAffectedHostIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateAffectedVolumeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateAffectedPopIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateVulnerabilityFindingIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateOccurredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateDiscoveredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateResolvedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateReporterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateReferenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateSourceItemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateNotificationOpenedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateNotificationClosedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsCreateProviderEntityErrorComponent):
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
        from ..models.api_v1_incidents_create_actual_availability_error_component import (
            ApiV1IncidentsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_incidents_create_affected_host_ids_error_component import (
            ApiV1IncidentsCreateAffectedHostIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_affected_pop_ids_error_component import (
            ApiV1IncidentsCreateAffectedPopIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_affected_volume_ids_error_component import (
            ApiV1IncidentsCreateAffectedVolumeIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_annotations_error_component import (
            ApiV1IncidentsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_incidents_create_archived_at_error_component import (
            ApiV1IncidentsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_incidents_create_archived_by_error_component import (
            ApiV1IncidentsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_incidents_create_archived_error_component import ApiV1IncidentsCreateArchivedErrorComponent
        from ..models.api_v1_incidents_create_archived_reason_error_component import (
            ApiV1IncidentsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_incidents_create_created_by_component_error_component import (
            ApiV1IncidentsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_incidents_create_created_by_user_error_component import (
            ApiV1IncidentsCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_incidents_create_criticality_error_component import (
            ApiV1IncidentsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_incidents_create_debug_mode_error_component import (
            ApiV1IncidentsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_incidents_create_discovered_at_error_component import (
            ApiV1IncidentsCreateDiscoveredAtErrorComponent,
        )
        from ..models.api_v1_incidents_create_discovery_enabled_error_component import (
            ApiV1IncidentsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_incidents_create_display_name_error_component import (
            ApiV1IncidentsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_incidents_create_downtime_ids_error_component import (
            ApiV1IncidentsCreateDowntimeIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_kind_error_component import ApiV1IncidentsCreateKindErrorComponent
        from ..models.api_v1_incidents_create_labels_error_component import ApiV1IncidentsCreateLabelsErrorComponent
        from ..models.api_v1_incidents_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1IncidentsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_incidents_create_managed_by_content_type_error_component import (
            ApiV1IncidentsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_incidents_create_managed_by_object_id_error_component import (
            ApiV1IncidentsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_incidents_create_modified_by_user_error_component import (
            ApiV1IncidentsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_incidents_create_name_error_component import ApiV1IncidentsCreateNameErrorComponent
        from ..models.api_v1_incidents_create_non_field_errors_error_component import (
            ApiV1IncidentsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_incidents_create_notification_closed_sent_error_component import (
            ApiV1IncidentsCreateNotificationClosedSentErrorComponent,
        )
        from ..models.api_v1_incidents_create_notification_opened_sent_error_component import (
            ApiV1IncidentsCreateNotificationOpenedSentErrorComponent,
        )
        from ..models.api_v1_incidents_create_occurred_at_error_component import (
            ApiV1IncidentsCreateOccurredAtErrorComponent,
        )
        from ..models.api_v1_incidents_create_organization_id_error_component import (
            ApiV1IncidentsCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_incidents_create_platform_dns_record_created_error_component import (
            ApiV1IncidentsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_incidents_create_platform_service_error_component import (
            ApiV1IncidentsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_incidents_create_provider_entity_error_component import (
            ApiV1IncidentsCreateProviderEntityErrorComponent,
        )
        from ..models.api_v1_incidents_create_provider_error_component import ApiV1IncidentsCreateProviderErrorComponent
        from ..models.api_v1_incidents_create_provider_id_error_component import (
            ApiV1IncidentsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_incidents_create_provider_reference_error_component import (
            ApiV1IncidentsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_incidents_create_reconciliation_enabled_error_component import (
            ApiV1IncidentsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_incidents_create_reference_url_error_component import (
            ApiV1IncidentsCreateReferenceUrlErrorComponent,
        )
        from ..models.api_v1_incidents_create_reporter_error_component import ApiV1IncidentsCreateReporterErrorComponent
        from ..models.api_v1_incidents_create_resolved_at_error_component import (
            ApiV1IncidentsCreateResolvedAtErrorComponent,
        )
        from ..models.api_v1_incidents_create_scope_error_component import ApiV1IncidentsCreateScopeErrorComponent
        from ..models.api_v1_incidents_create_sla_availability_error_component import (
            ApiV1IncidentsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_incidents_create_sla_target_error_component import (
            ApiV1IncidentsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_incidents_create_sla_window_days_error_component import (
            ApiV1IncidentsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_incidents_create_slo_availability_error_component import (
            ApiV1IncidentsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_incidents_create_slo_target_error_component import (
            ApiV1IncidentsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_incidents_create_slo_window_days_error_component import (
            ApiV1IncidentsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_incidents_create_source_datasource_error_component import (
            ApiV1IncidentsCreateSourceDatasourceErrorComponent,
        )
        from ..models.api_v1_incidents_create_source_item_id_error_component import (
            ApiV1IncidentsCreateSourceItemIdErrorComponent,
        )
        from ..models.api_v1_incidents_create_status_error_component import ApiV1IncidentsCreateStatusErrorComponent
        from ..models.api_v1_incidents_create_target_availability_error_component import (
            ApiV1IncidentsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_incidents_create_vulnerability_finding_ids_error_component import (
            ApiV1IncidentsCreateVulnerabilityFindingIdsErrorComponent,
        )
        from ..models.api_v1_incidents_create_workspace_id_error_component import (
            ApiV1IncidentsCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IncidentsCreateActualAvailabilityErrorComponent
                | ApiV1IncidentsCreateAffectedHostIdsErrorComponent
                | ApiV1IncidentsCreateAffectedPopIdsErrorComponent
                | ApiV1IncidentsCreateAffectedVolumeIdsErrorComponent
                | ApiV1IncidentsCreateAnnotationsErrorComponent
                | ApiV1IncidentsCreateArchivedAtErrorComponent
                | ApiV1IncidentsCreateArchivedByErrorComponent
                | ApiV1IncidentsCreateArchivedErrorComponent
                | ApiV1IncidentsCreateArchivedReasonErrorComponent
                | ApiV1IncidentsCreateCreatedByComponentErrorComponent
                | ApiV1IncidentsCreateCreatedByUserErrorComponent
                | ApiV1IncidentsCreateCriticalityErrorComponent
                | ApiV1IncidentsCreateDebugModeErrorComponent
                | ApiV1IncidentsCreateDiscoveredAtErrorComponent
                | ApiV1IncidentsCreateDiscoveryEnabledErrorComponent
                | ApiV1IncidentsCreateDisplayNameErrorComponent
                | ApiV1IncidentsCreateDowntimeIdsErrorComponent
                | ApiV1IncidentsCreateKindErrorComponent
                | ApiV1IncidentsCreateLabelsErrorComponent
                | ApiV1IncidentsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1IncidentsCreateManagedByContentTypeErrorComponent
                | ApiV1IncidentsCreateManagedByObjectIdErrorComponent
                | ApiV1IncidentsCreateModifiedByUserErrorComponent
                | ApiV1IncidentsCreateNameErrorComponent
                | ApiV1IncidentsCreateNonFieldErrorsErrorComponent
                | ApiV1IncidentsCreateNotificationClosedSentErrorComponent
                | ApiV1IncidentsCreateNotificationOpenedSentErrorComponent
                | ApiV1IncidentsCreateOccurredAtErrorComponent
                | ApiV1IncidentsCreateOrganizationIdErrorComponent
                | ApiV1IncidentsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1IncidentsCreatePlatformServiceErrorComponent
                | ApiV1IncidentsCreateProviderEntityErrorComponent
                | ApiV1IncidentsCreateProviderErrorComponent
                | ApiV1IncidentsCreateProviderIdErrorComponent
                | ApiV1IncidentsCreateProviderReferenceErrorComponent
                | ApiV1IncidentsCreateReconciliationEnabledErrorComponent
                | ApiV1IncidentsCreateReferenceUrlErrorComponent
                | ApiV1IncidentsCreateReporterErrorComponent
                | ApiV1IncidentsCreateResolvedAtErrorComponent
                | ApiV1IncidentsCreateScopeErrorComponent
                | ApiV1IncidentsCreateSlaAvailabilityErrorComponent
                | ApiV1IncidentsCreateSlaTargetErrorComponent
                | ApiV1IncidentsCreateSlaWindowDaysErrorComponent
                | ApiV1IncidentsCreateSloAvailabilityErrorComponent
                | ApiV1IncidentsCreateSloTargetErrorComponent
                | ApiV1IncidentsCreateSloWindowDaysErrorComponent
                | ApiV1IncidentsCreateSourceDatasourceErrorComponent
                | ApiV1IncidentsCreateSourceItemIdErrorComponent
                | ApiV1IncidentsCreateStatusErrorComponent
                | ApiV1IncidentsCreateTargetAvailabilityErrorComponent
                | ApiV1IncidentsCreateVulnerabilityFindingIdsErrorComponent
                | ApiV1IncidentsCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_0 = (
                        ApiV1IncidentsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_1 = (
                        ApiV1IncidentsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_2 = (
                        ApiV1IncidentsCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_3 = (
                        ApiV1IncidentsCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_4 = (
                        ApiV1IncidentsCreateDowntimeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_5 = (
                        ApiV1IncidentsCreateAffectedHostIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_6 = (
                        ApiV1IncidentsCreateAffectedVolumeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_7 = (
                        ApiV1IncidentsCreateAffectedPopIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_8 = (
                        ApiV1IncidentsCreateVulnerabilityFindingIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_9 = (
                        ApiV1IncidentsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_10 = (
                        ApiV1IncidentsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_11 = (
                        ApiV1IncidentsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_12 = (
                        ApiV1IncidentsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_13 = (
                        ApiV1IncidentsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_14 = (
                        ApiV1IncidentsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_15 = (
                        ApiV1IncidentsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_16 = (
                        ApiV1IncidentsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_17 = (
                        ApiV1IncidentsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_18 = (
                        ApiV1IncidentsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_19 = (
                        ApiV1IncidentsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_20 = (
                        ApiV1IncidentsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_21 = (
                        ApiV1IncidentsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_22 = (
                        ApiV1IncidentsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_23 = (
                        ApiV1IncidentsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_24 = (
                        ApiV1IncidentsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_25 = (
                        ApiV1IncidentsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_26 = (
                        ApiV1IncidentsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_27 = (
                        ApiV1IncidentsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_28 = (
                        ApiV1IncidentsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_29 = (
                        ApiV1IncidentsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_30 = (
                        ApiV1IncidentsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_31 = (
                        ApiV1IncidentsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_32 = (
                        ApiV1IncidentsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_33 = (
                        ApiV1IncidentsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_34 = (
                        ApiV1IncidentsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_35 = (
                        ApiV1IncidentsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_36 = (
                        ApiV1IncidentsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_37 = (
                        ApiV1IncidentsCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_38 = (
                        ApiV1IncidentsCreateOccurredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_39 = (
                        ApiV1IncidentsCreateDiscoveredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_40 = (
                        ApiV1IncidentsCreateResolvedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_41 = (
                        ApiV1IncidentsCreateReporterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_42 = (
                        ApiV1IncidentsCreateReferenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_43 = (
                        ApiV1IncidentsCreateSourceItemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_44 = (
                        ApiV1IncidentsCreateNotificationOpenedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_45 = (
                        ApiV1IncidentsCreateNotificationClosedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_46 = (
                        ApiV1IncidentsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_47 = (
                        ApiV1IncidentsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_48 = (
                        ApiV1IncidentsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_49 = (
                        ApiV1IncidentsCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_create_error_type_50 = (
                        ApiV1IncidentsCreateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_incidents_create_error_type_51 = (
                    ApiV1IncidentsCreateSourceDatasourceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_incidents_create_error_type_51

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_incidents_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_incidents_create_validation_error.additional_properties = d
        return api_v1_incidents_create_validation_error

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
