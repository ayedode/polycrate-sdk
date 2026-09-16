from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_endpoints_partial_update_actual_availability_error_component import (
        ApiV1EndpointsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_annotations_error_component import (
        ApiV1EndpointsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_archived_at_error_component import (
        ApiV1EndpointsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_archived_by_error_component import (
        ApiV1EndpointsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_archived_error_component import (
        ApiV1EndpointsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_archived_reason_error_component import (
        ApiV1EndpointsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_check_result_retention_days_error_component import (
        ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_check_results_error_component import (
        ApiV1EndpointsPartialUpdateCheckResultsErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_created_by_component_error_component import (
        ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_created_by_user_error_component import (
        ApiV1EndpointsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_criticality_error_component import (
        ApiV1EndpointsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_debug_mode_error_component import (
        ApiV1EndpointsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_discovery_enabled_error_component import (
        ApiV1EndpointsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_display_name_error_component import (
        ApiV1EndpointsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_do_not_monitor_error_component import (
        ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_k8s_app_error_component import (
        ApiV1EndpointsPartialUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_k8s_cluster_error_component import (
        ApiV1EndpointsPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_kind_error_component import (
        ApiV1EndpointsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_labels_error_component import (
        ApiV1EndpointsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_last_agent_metrics_error_component import (
        ApiV1EndpointsPartialUpdateLastAgentMetricsErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1EndpointsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_loadbalancer_instance_error_component import (
        ApiV1EndpointsPartialUpdateLoadbalancerInstanceErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_managed_by_content_type_error_component import (
        ApiV1EndpointsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_managed_by_object_id_error_component import (
        ApiV1EndpointsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_max_agents_per_endpoint_error_component import (
        ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_modified_by_user_error_component import (
        ApiV1EndpointsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_name_error_component import (
        ApiV1EndpointsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_non_field_errors_error_component import (
        ApiV1EndpointsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_organization_id_error_component import (
        ApiV1EndpointsPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_platform_dns_record_created_error_component import (
        ApiV1EndpointsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_platform_service_error_component import (
        ApiV1EndpointsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_pop_endpoint_error_component import (
        ApiV1EndpointsPartialUpdatePopEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_provider_error_component import (
        ApiV1EndpointsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_provider_id_error_component import (
        ApiV1EndpointsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_provider_reference_error_component import (
        ApiV1EndpointsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_reconciliation_enabled_error_component import (
        ApiV1EndpointsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_region_error_component import (
        ApiV1EndpointsPartialUpdateRegionErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_remote_address_error_component import (
        ApiV1EndpointsPartialUpdateRemoteAddressErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_remote_port_error_component import (
        ApiV1EndpointsPartialUpdateRemotePortErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_resolved_ip_error_component import (
        ApiV1EndpointsPartialUpdateResolvedIpErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_s3_cluster_error_component import (
        ApiV1EndpointsPartialUpdateS3ClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_scope_error_component import (
        ApiV1EndpointsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_sla_availability_error_component import (
        ApiV1EndpointsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_sla_target_error_component import (
        ApiV1EndpointsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_sla_window_days_error_component import (
        ApiV1EndpointsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_slo_availability_error_component import (
        ApiV1EndpointsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_slo_target_error_component import (
        ApiV1EndpointsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_slo_window_days_error_component import (
        ApiV1EndpointsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_spec_error_component import (
        ApiV1EndpointsPartialUpdateSpecErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_target_availability_error_component import (
        ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_partial_update_workspace_id_error_component import (
        ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1EndpointsPartialUpdateValidationError")


@_attrs_define
class ApiV1EndpointsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1EndpointsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1EndpointsPartialUpdateAnnotationsErrorComponent | ApiV1EndpointsPartialUpdateArchivedAtErrorComponent |
            ApiV1EndpointsPartialUpdateArchivedByErrorComponent | ApiV1EndpointsPartialUpdateArchivedErrorComponent |
            ApiV1EndpointsPartialUpdateArchivedReasonErrorComponent |
            ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponent |
            ApiV1EndpointsPartialUpdateCheckResultsErrorComponent |
            ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1EndpointsPartialUpdateCreatedByUserErrorComponent | ApiV1EndpointsPartialUpdateCriticalityErrorComponent |
            ApiV1EndpointsPartialUpdateDebugModeErrorComponent | ApiV1EndpointsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1EndpointsPartialUpdateDisplayNameErrorComponent | ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponent |
            ApiV1EndpointsPartialUpdateK8SAppErrorComponent | ApiV1EndpointsPartialUpdateK8SClusterErrorComponent |
            ApiV1EndpointsPartialUpdateKindErrorComponent | ApiV1EndpointsPartialUpdateLabelsErrorComponent |
            ApiV1EndpointsPartialUpdateLastAgentMetricsErrorComponent |
            ApiV1EndpointsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1EndpointsPartialUpdateLoadbalancerInstanceErrorComponent |
            ApiV1EndpointsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1EndpointsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponent |
            ApiV1EndpointsPartialUpdateModifiedByUserErrorComponent | ApiV1EndpointsPartialUpdateNameErrorComponent |
            ApiV1EndpointsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1EndpointsPartialUpdateOrganizationIdErrorComponent |
            ApiV1EndpointsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1EndpointsPartialUpdatePlatformServiceErrorComponent | ApiV1EndpointsPartialUpdatePopEndpointErrorComponent
            | ApiV1EndpointsPartialUpdateProviderErrorComponent | ApiV1EndpointsPartialUpdateProviderIdErrorComponent |
            ApiV1EndpointsPartialUpdateProviderReferenceErrorComponent |
            ApiV1EndpointsPartialUpdateReconciliationEnabledErrorComponent | ApiV1EndpointsPartialUpdateRegionErrorComponent
            | ApiV1EndpointsPartialUpdateRemoteAddressErrorComponent | ApiV1EndpointsPartialUpdateRemotePortErrorComponent |
            ApiV1EndpointsPartialUpdateResolvedIpErrorComponent | ApiV1EndpointsPartialUpdateS3ClusterErrorComponent |
            ApiV1EndpointsPartialUpdateScopeErrorComponent | ApiV1EndpointsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1EndpointsPartialUpdateSlaTargetErrorComponent | ApiV1EndpointsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1EndpointsPartialUpdateSloAvailabilityErrorComponent | ApiV1EndpointsPartialUpdateSloTargetErrorComponent |
            ApiV1EndpointsPartialUpdateSloWindowDaysErrorComponent | ApiV1EndpointsPartialUpdateSpecErrorComponent |
            ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1EndpointsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1EndpointsPartialUpdateAnnotationsErrorComponent
        | ApiV1EndpointsPartialUpdateArchivedAtErrorComponent
        | ApiV1EndpointsPartialUpdateArchivedByErrorComponent
        | ApiV1EndpointsPartialUpdateArchivedErrorComponent
        | ApiV1EndpointsPartialUpdateArchivedReasonErrorComponent
        | ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponent
        | ApiV1EndpointsPartialUpdateCheckResultsErrorComponent
        | ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1EndpointsPartialUpdateCreatedByUserErrorComponent
        | ApiV1EndpointsPartialUpdateCriticalityErrorComponent
        | ApiV1EndpointsPartialUpdateDebugModeErrorComponent
        | ApiV1EndpointsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1EndpointsPartialUpdateDisplayNameErrorComponent
        | ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponent
        | ApiV1EndpointsPartialUpdateK8SAppErrorComponent
        | ApiV1EndpointsPartialUpdateK8SClusterErrorComponent
        | ApiV1EndpointsPartialUpdateKindErrorComponent
        | ApiV1EndpointsPartialUpdateLabelsErrorComponent
        | ApiV1EndpointsPartialUpdateLastAgentMetricsErrorComponent
        | ApiV1EndpointsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1EndpointsPartialUpdateLoadbalancerInstanceErrorComponent
        | ApiV1EndpointsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1EndpointsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponent
        | ApiV1EndpointsPartialUpdateModifiedByUserErrorComponent
        | ApiV1EndpointsPartialUpdateNameErrorComponent
        | ApiV1EndpointsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1EndpointsPartialUpdateOrganizationIdErrorComponent
        | ApiV1EndpointsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1EndpointsPartialUpdatePlatformServiceErrorComponent
        | ApiV1EndpointsPartialUpdatePopEndpointErrorComponent
        | ApiV1EndpointsPartialUpdateProviderErrorComponent
        | ApiV1EndpointsPartialUpdateProviderIdErrorComponent
        | ApiV1EndpointsPartialUpdateProviderReferenceErrorComponent
        | ApiV1EndpointsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1EndpointsPartialUpdateRegionErrorComponent
        | ApiV1EndpointsPartialUpdateRemoteAddressErrorComponent
        | ApiV1EndpointsPartialUpdateRemotePortErrorComponent
        | ApiV1EndpointsPartialUpdateResolvedIpErrorComponent
        | ApiV1EndpointsPartialUpdateS3ClusterErrorComponent
        | ApiV1EndpointsPartialUpdateScopeErrorComponent
        | ApiV1EndpointsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1EndpointsPartialUpdateSlaTargetErrorComponent
        | ApiV1EndpointsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1EndpointsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1EndpointsPartialUpdateSloTargetErrorComponent
        | ApiV1EndpointsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1EndpointsPartialUpdateSpecErrorComponent
        | ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_endpoints_partial_update_actual_availability_error_component import (
            ApiV1EndpointsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_annotations_error_component import (
            ApiV1EndpointsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_archived_at_error_component import (
            ApiV1EndpointsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_archived_by_error_component import (
            ApiV1EndpointsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_archived_error_component import (
            ApiV1EndpointsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_archived_reason_error_component import (
            ApiV1EndpointsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_check_result_retention_days_error_component import (
            ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_check_results_error_component import (
            ApiV1EndpointsPartialUpdateCheckResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_created_by_component_error_component import (
            ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_created_by_user_error_component import (
            ApiV1EndpointsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_criticality_error_component import (
            ApiV1EndpointsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_debug_mode_error_component import (
            ApiV1EndpointsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_discovery_enabled_error_component import (
            ApiV1EndpointsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_display_name_error_component import (
            ApiV1EndpointsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_do_not_monitor_error_component import (
            ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_k8s_app_error_component import (
            ApiV1EndpointsPartialUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_k8s_cluster_error_component import (
            ApiV1EndpointsPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_kind_error_component import (
            ApiV1EndpointsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_labels_error_component import (
            ApiV1EndpointsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_last_agent_metrics_error_component import (
            ApiV1EndpointsPartialUpdateLastAgentMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_managed_by_content_type_error_component import (
            ApiV1EndpointsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_managed_by_object_id_error_component import (
            ApiV1EndpointsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_modified_by_user_error_component import (
            ApiV1EndpointsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_name_error_component import (
            ApiV1EndpointsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_non_field_errors_error_component import (
            ApiV1EndpointsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_organization_id_error_component import (
            ApiV1EndpointsPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_platform_dns_record_created_error_component import (
            ApiV1EndpointsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_platform_service_error_component import (
            ApiV1EndpointsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_pop_endpoint_error_component import (
            ApiV1EndpointsPartialUpdatePopEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_provider_error_component import (
            ApiV1EndpointsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_provider_id_error_component import (
            ApiV1EndpointsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_provider_reference_error_component import (
            ApiV1EndpointsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_reconciliation_enabled_error_component import (
            ApiV1EndpointsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_region_error_component import (
            ApiV1EndpointsPartialUpdateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_remote_address_error_component import (
            ApiV1EndpointsPartialUpdateRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_remote_port_error_component import (
            ApiV1EndpointsPartialUpdateRemotePortErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_resolved_ip_error_component import (
            ApiV1EndpointsPartialUpdateResolvedIpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_s3_cluster_error_component import (
            ApiV1EndpointsPartialUpdateS3ClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_scope_error_component import (
            ApiV1EndpointsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_sla_availability_error_component import (
            ApiV1EndpointsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_sla_target_error_component import (
            ApiV1EndpointsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_sla_window_days_error_component import (
            ApiV1EndpointsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_slo_availability_error_component import (
            ApiV1EndpointsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_slo_target_error_component import (
            ApiV1EndpointsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_slo_window_days_error_component import (
            ApiV1EndpointsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_spec_error_component import (
            ApiV1EndpointsPartialUpdateSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_target_availability_error_component import (
            ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_workspace_id_error_component import (
            ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1EndpointsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1EndpointsPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateRemoteAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateRemotePortErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateCheckResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdatePopEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateLastAgentMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateResolvedIpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateS3ClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsPartialUpdateRegionErrorComponent):
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
        from ..models.api_v1_endpoints_partial_update_actual_availability_error_component import (
            ApiV1EndpointsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_annotations_error_component import (
            ApiV1EndpointsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_archived_at_error_component import (
            ApiV1EndpointsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_archived_by_error_component import (
            ApiV1EndpointsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_archived_error_component import (
            ApiV1EndpointsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_archived_reason_error_component import (
            ApiV1EndpointsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_check_result_retention_days_error_component import (
            ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_check_results_error_component import (
            ApiV1EndpointsPartialUpdateCheckResultsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_created_by_component_error_component import (
            ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_created_by_user_error_component import (
            ApiV1EndpointsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_criticality_error_component import (
            ApiV1EndpointsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_debug_mode_error_component import (
            ApiV1EndpointsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_discovery_enabled_error_component import (
            ApiV1EndpointsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_display_name_error_component import (
            ApiV1EndpointsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_do_not_monitor_error_component import (
            ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_k8s_app_error_component import (
            ApiV1EndpointsPartialUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_k8s_cluster_error_component import (
            ApiV1EndpointsPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_kind_error_component import (
            ApiV1EndpointsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_labels_error_component import (
            ApiV1EndpointsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_last_agent_metrics_error_component import (
            ApiV1EndpointsPartialUpdateLastAgentMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_loadbalancer_instance_error_component import (
            ApiV1EndpointsPartialUpdateLoadbalancerInstanceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_managed_by_content_type_error_component import (
            ApiV1EndpointsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_managed_by_object_id_error_component import (
            ApiV1EndpointsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_modified_by_user_error_component import (
            ApiV1EndpointsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_name_error_component import (
            ApiV1EndpointsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_non_field_errors_error_component import (
            ApiV1EndpointsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_organization_id_error_component import (
            ApiV1EndpointsPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_platform_dns_record_created_error_component import (
            ApiV1EndpointsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_platform_service_error_component import (
            ApiV1EndpointsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_pop_endpoint_error_component import (
            ApiV1EndpointsPartialUpdatePopEndpointErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_provider_error_component import (
            ApiV1EndpointsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_provider_id_error_component import (
            ApiV1EndpointsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_provider_reference_error_component import (
            ApiV1EndpointsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_reconciliation_enabled_error_component import (
            ApiV1EndpointsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_region_error_component import (
            ApiV1EndpointsPartialUpdateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_remote_address_error_component import (
            ApiV1EndpointsPartialUpdateRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_remote_port_error_component import (
            ApiV1EndpointsPartialUpdateRemotePortErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_resolved_ip_error_component import (
            ApiV1EndpointsPartialUpdateResolvedIpErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_s3_cluster_error_component import (
            ApiV1EndpointsPartialUpdateS3ClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_scope_error_component import (
            ApiV1EndpointsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_sla_availability_error_component import (
            ApiV1EndpointsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_sla_target_error_component import (
            ApiV1EndpointsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_sla_window_days_error_component import (
            ApiV1EndpointsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_slo_availability_error_component import (
            ApiV1EndpointsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_slo_target_error_component import (
            ApiV1EndpointsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_slo_window_days_error_component import (
            ApiV1EndpointsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_spec_error_component import (
            ApiV1EndpointsPartialUpdateSpecErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_target_availability_error_component import (
            ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_endpoints_partial_update_workspace_id_error_component import (
            ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1EndpointsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1EndpointsPartialUpdateAnnotationsErrorComponent
                | ApiV1EndpointsPartialUpdateArchivedAtErrorComponent
                | ApiV1EndpointsPartialUpdateArchivedByErrorComponent
                | ApiV1EndpointsPartialUpdateArchivedErrorComponent
                | ApiV1EndpointsPartialUpdateArchivedReasonErrorComponent
                | ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponent
                | ApiV1EndpointsPartialUpdateCheckResultsErrorComponent
                | ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1EndpointsPartialUpdateCreatedByUserErrorComponent
                | ApiV1EndpointsPartialUpdateCriticalityErrorComponent
                | ApiV1EndpointsPartialUpdateDebugModeErrorComponent
                | ApiV1EndpointsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1EndpointsPartialUpdateDisplayNameErrorComponent
                | ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponent
                | ApiV1EndpointsPartialUpdateK8SAppErrorComponent
                | ApiV1EndpointsPartialUpdateK8SClusterErrorComponent
                | ApiV1EndpointsPartialUpdateKindErrorComponent
                | ApiV1EndpointsPartialUpdateLabelsErrorComponent
                | ApiV1EndpointsPartialUpdateLastAgentMetricsErrorComponent
                | ApiV1EndpointsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1EndpointsPartialUpdateLoadbalancerInstanceErrorComponent
                | ApiV1EndpointsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1EndpointsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponent
                | ApiV1EndpointsPartialUpdateModifiedByUserErrorComponent
                | ApiV1EndpointsPartialUpdateNameErrorComponent
                | ApiV1EndpointsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1EndpointsPartialUpdateOrganizationIdErrorComponent
                | ApiV1EndpointsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1EndpointsPartialUpdatePlatformServiceErrorComponent
                | ApiV1EndpointsPartialUpdatePopEndpointErrorComponent
                | ApiV1EndpointsPartialUpdateProviderErrorComponent
                | ApiV1EndpointsPartialUpdateProviderIdErrorComponent
                | ApiV1EndpointsPartialUpdateProviderReferenceErrorComponent
                | ApiV1EndpointsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1EndpointsPartialUpdateRegionErrorComponent
                | ApiV1EndpointsPartialUpdateRemoteAddressErrorComponent
                | ApiV1EndpointsPartialUpdateRemotePortErrorComponent
                | ApiV1EndpointsPartialUpdateResolvedIpErrorComponent
                | ApiV1EndpointsPartialUpdateS3ClusterErrorComponent
                | ApiV1EndpointsPartialUpdateScopeErrorComponent
                | ApiV1EndpointsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1EndpointsPartialUpdateSlaTargetErrorComponent
                | ApiV1EndpointsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1EndpointsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1EndpointsPartialUpdateSloTargetErrorComponent
                | ApiV1EndpointsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1EndpointsPartialUpdateSpecErrorComponent
                | ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_0 = (
                        ApiV1EndpointsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_1 = (
                        ApiV1EndpointsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_2 = (
                        ApiV1EndpointsPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_3 = (
                        ApiV1EndpointsPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_4 = (
                        ApiV1EndpointsPartialUpdateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_5 = (
                        ApiV1EndpointsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_6 = (
                        ApiV1EndpointsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_7 = (
                        ApiV1EndpointsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_8 = (
                        ApiV1EndpointsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_9 = (
                        ApiV1EndpointsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_10 = (
                        ApiV1EndpointsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_11 = (
                        ApiV1EndpointsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_12 = (
                        ApiV1EndpointsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_13 = (
                        ApiV1EndpointsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_14 = (
                        ApiV1EndpointsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_15 = (
                        ApiV1EndpointsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_16 = (
                        ApiV1EndpointsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_17 = (
                        ApiV1EndpointsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_18 = (
                        ApiV1EndpointsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_19 = (
                        ApiV1EndpointsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_20 = (
                        ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_21 = (
                        ApiV1EndpointsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_22 = (
                        ApiV1EndpointsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_23 = (
                        ApiV1EndpointsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_24 = (
                        ApiV1EndpointsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_25 = (
                        ApiV1EndpointsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_26 = (
                        ApiV1EndpointsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_27 = (
                        ApiV1EndpointsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_28 = (
                        ApiV1EndpointsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_29 = (
                        ApiV1EndpointsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_30 = (
                        ApiV1EndpointsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_31 = (
                        ApiV1EndpointsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_32 = (
                        ApiV1EndpointsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_33 = (
                        ApiV1EndpointsPartialUpdateRemoteAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_34 = (
                        ApiV1EndpointsPartialUpdateRemotePortErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_35 = (
                        ApiV1EndpointsPartialUpdateCheckResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_36 = (
                        ApiV1EndpointsPartialUpdateDoNotMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_37 = (
                        ApiV1EndpointsPartialUpdatePopEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_38 = (
                        ApiV1EndpointsPartialUpdateLastAgentMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_39 = (
                        ApiV1EndpointsPartialUpdateResolvedIpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_40 = (
                        ApiV1EndpointsPartialUpdateMaxAgentsPerEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_41 = (
                        ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_42 = (
                        ApiV1EndpointsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_43 = (
                        ApiV1EndpointsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_44 = (
                        ApiV1EndpointsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_45 = (
                        ApiV1EndpointsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_46 = (
                        ApiV1EndpointsPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_47 = (
                        ApiV1EndpointsPartialUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_48 = (
                        ApiV1EndpointsPartialUpdateS3ClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_partial_update_error_type_49 = (
                        ApiV1EndpointsPartialUpdateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_partial_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_endpoints_partial_update_error_type_50 = (
                    ApiV1EndpointsPartialUpdateLoadbalancerInstanceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_endpoints_partial_update_error_type_50

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_endpoints_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_endpoints_partial_update_validation_error.additional_properties = d
        return api_v1_endpoints_partial_update_validation_error

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
