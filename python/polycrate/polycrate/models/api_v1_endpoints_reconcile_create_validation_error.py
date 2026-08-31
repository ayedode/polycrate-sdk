from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_endpoints_reconcile_create_actual_availability_error_component import (
        ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_annotations_error_component import (
        ApiV1EndpointsReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_archived_at_error_component import (
        ApiV1EndpointsReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_archived_by_error_component import (
        ApiV1EndpointsReconcileCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_archived_error_component import (
        ApiV1EndpointsReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_archived_reason_error_component import (
        ApiV1EndpointsReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_check_result_retention_days_error_component import (
        ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_check_results_error_component import (
        ApiV1EndpointsReconcileCreateCheckResultsErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_created_by_component_error_component import (
        ApiV1EndpointsReconcileCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_created_by_user_error_component import (
        ApiV1EndpointsReconcileCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_criticality_error_component import (
        ApiV1EndpointsReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_debug_mode_error_component import (
        ApiV1EndpointsReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_discovery_enabled_error_component import (
        ApiV1EndpointsReconcileCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_display_name_error_component import (
        ApiV1EndpointsReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_do_not_monitor_error_component import (
        ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_k8s_app_error_component import (
        ApiV1EndpointsReconcileCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_k8s_cluster_error_component import (
        ApiV1EndpointsReconcileCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_kind_error_component import (
        ApiV1EndpointsReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_labels_error_component import (
        ApiV1EndpointsReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_last_agent_metrics_error_component import (
        ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1EndpointsReconcileCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_loadbalancer_instance_error_component import (
        ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_managed_by_content_type_error_component import (
        ApiV1EndpointsReconcileCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_managed_by_object_id_error_component import (
        ApiV1EndpointsReconcileCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_max_agents_per_endpoint_error_component import (
        ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_modified_by_user_error_component import (
        ApiV1EndpointsReconcileCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_name_error_component import (
        ApiV1EndpointsReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_non_field_errors_error_component import (
        ApiV1EndpointsReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_organization_id_error_component import (
        ApiV1EndpointsReconcileCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_platform_dns_record_created_error_component import (
        ApiV1EndpointsReconcileCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_platform_service_error_component import (
        ApiV1EndpointsReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_pop_endpoint_error_component import (
        ApiV1EndpointsReconcileCreatePopEndpointErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_provider_error_component import (
        ApiV1EndpointsReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_provider_id_error_component import (
        ApiV1EndpointsReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_provider_reference_error_component import (
        ApiV1EndpointsReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_region_error_component import (
        ApiV1EndpointsReconcileCreateRegionErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_remote_address_error_component import (
        ApiV1EndpointsReconcileCreateRemoteAddressErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_remote_port_error_component import (
        ApiV1EndpointsReconcileCreateRemotePortErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_resolved_ip_error_component import (
        ApiV1EndpointsReconcileCreateResolvedIpErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_s3_cluster_error_component import (
        ApiV1EndpointsReconcileCreateS3ClusterErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_scope_error_component import (
        ApiV1EndpointsReconcileCreateScopeErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_sla_availability_error_component import (
        ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_sla_target_error_component import (
        ApiV1EndpointsReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_sla_window_days_error_component import (
        ApiV1EndpointsReconcileCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_slo_availability_error_component import (
        ApiV1EndpointsReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_slo_target_error_component import (
        ApiV1EndpointsReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_slo_window_days_error_component import (
        ApiV1EndpointsReconcileCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_spec_error_component import (
        ApiV1EndpointsReconcileCreateSpecErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_target_availability_error_component import (
        ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_endpoints_reconcile_create_workspace_id_error_component import (
        ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1EndpointsReconcileCreateValidationError")


@_attrs_define
class ApiV1EndpointsReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponent |
            ApiV1EndpointsReconcileCreateAnnotationsErrorComponent | ApiV1EndpointsReconcileCreateArchivedAtErrorComponent |
            ApiV1EndpointsReconcileCreateArchivedByErrorComponent | ApiV1EndpointsReconcileCreateArchivedErrorComponent |
            ApiV1EndpointsReconcileCreateArchivedReasonErrorComponent |
            ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponent |
            ApiV1EndpointsReconcileCreateCheckResultsErrorComponent |
            ApiV1EndpointsReconcileCreateCreatedByComponentErrorComponent |
            ApiV1EndpointsReconcileCreateCreatedByUserErrorComponent |
            ApiV1EndpointsReconcileCreateCriticalityErrorComponent | ApiV1EndpointsReconcileCreateDebugModeErrorComponent |
            ApiV1EndpointsReconcileCreateDiscoveryEnabledErrorComponent |
            ApiV1EndpointsReconcileCreateDisplayNameErrorComponent | ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponent
            | ApiV1EndpointsReconcileCreateK8SAppErrorComponent | ApiV1EndpointsReconcileCreateK8SClusterErrorComponent |
            ApiV1EndpointsReconcileCreateKindErrorComponent | ApiV1EndpointsReconcileCreateLabelsErrorComponent |
            ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponent |
            ApiV1EndpointsReconcileCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponent |
            ApiV1EndpointsReconcileCreateManagedByContentTypeErrorComponent |
            ApiV1EndpointsReconcileCreateManagedByObjectIdErrorComponent |
            ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponent |
            ApiV1EndpointsReconcileCreateModifiedByUserErrorComponent | ApiV1EndpointsReconcileCreateNameErrorComponent |
            ApiV1EndpointsReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1EndpointsReconcileCreateOrganizationIdErrorComponent |
            ApiV1EndpointsReconcileCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1EndpointsReconcileCreatePlatformServiceErrorComponent |
            ApiV1EndpointsReconcileCreatePopEndpointErrorComponent | ApiV1EndpointsReconcileCreateProviderErrorComponent |
            ApiV1EndpointsReconcileCreateProviderIdErrorComponent |
            ApiV1EndpointsReconcileCreateProviderReferenceErrorComponent |
            ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1EndpointsReconcileCreateRegionErrorComponent | ApiV1EndpointsReconcileCreateRemoteAddressErrorComponent |
            ApiV1EndpointsReconcileCreateRemotePortErrorComponent | ApiV1EndpointsReconcileCreateResolvedIpErrorComponent |
            ApiV1EndpointsReconcileCreateS3ClusterErrorComponent | ApiV1EndpointsReconcileCreateScopeErrorComponent |
            ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1EndpointsReconcileCreateSlaTargetErrorComponent | ApiV1EndpointsReconcileCreateSlaWindowDaysErrorComponent
            | ApiV1EndpointsReconcileCreateSloAvailabilityErrorComponent |
            ApiV1EndpointsReconcileCreateSloTargetErrorComponent | ApiV1EndpointsReconcileCreateSloWindowDaysErrorComponent
            | ApiV1EndpointsReconcileCreateSpecErrorComponent |
            ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponent |
            ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponent
        | ApiV1EndpointsReconcileCreateAnnotationsErrorComponent
        | ApiV1EndpointsReconcileCreateArchivedAtErrorComponent
        | ApiV1EndpointsReconcileCreateArchivedByErrorComponent
        | ApiV1EndpointsReconcileCreateArchivedErrorComponent
        | ApiV1EndpointsReconcileCreateArchivedReasonErrorComponent
        | ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponent
        | ApiV1EndpointsReconcileCreateCheckResultsErrorComponent
        | ApiV1EndpointsReconcileCreateCreatedByComponentErrorComponent
        | ApiV1EndpointsReconcileCreateCreatedByUserErrorComponent
        | ApiV1EndpointsReconcileCreateCriticalityErrorComponent
        | ApiV1EndpointsReconcileCreateDebugModeErrorComponent
        | ApiV1EndpointsReconcileCreateDiscoveryEnabledErrorComponent
        | ApiV1EndpointsReconcileCreateDisplayNameErrorComponent
        | ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponent
        | ApiV1EndpointsReconcileCreateK8SAppErrorComponent
        | ApiV1EndpointsReconcileCreateK8SClusterErrorComponent
        | ApiV1EndpointsReconcileCreateKindErrorComponent
        | ApiV1EndpointsReconcileCreateLabelsErrorComponent
        | ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponent
        | ApiV1EndpointsReconcileCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponent
        | ApiV1EndpointsReconcileCreateManagedByContentTypeErrorComponent
        | ApiV1EndpointsReconcileCreateManagedByObjectIdErrorComponent
        | ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponent
        | ApiV1EndpointsReconcileCreateModifiedByUserErrorComponent
        | ApiV1EndpointsReconcileCreateNameErrorComponent
        | ApiV1EndpointsReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1EndpointsReconcileCreateOrganizationIdErrorComponent
        | ApiV1EndpointsReconcileCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1EndpointsReconcileCreatePlatformServiceErrorComponent
        | ApiV1EndpointsReconcileCreatePopEndpointErrorComponent
        | ApiV1EndpointsReconcileCreateProviderErrorComponent
        | ApiV1EndpointsReconcileCreateProviderIdErrorComponent
        | ApiV1EndpointsReconcileCreateProviderReferenceErrorComponent
        | ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1EndpointsReconcileCreateRegionErrorComponent
        | ApiV1EndpointsReconcileCreateRemoteAddressErrorComponent
        | ApiV1EndpointsReconcileCreateRemotePortErrorComponent
        | ApiV1EndpointsReconcileCreateResolvedIpErrorComponent
        | ApiV1EndpointsReconcileCreateS3ClusterErrorComponent
        | ApiV1EndpointsReconcileCreateScopeErrorComponent
        | ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1EndpointsReconcileCreateSlaTargetErrorComponent
        | ApiV1EndpointsReconcileCreateSlaWindowDaysErrorComponent
        | ApiV1EndpointsReconcileCreateSloAvailabilityErrorComponent
        | ApiV1EndpointsReconcileCreateSloTargetErrorComponent
        | ApiV1EndpointsReconcileCreateSloWindowDaysErrorComponent
        | ApiV1EndpointsReconcileCreateSpecErrorComponent
        | ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_endpoints_reconcile_create_actual_availability_error_component import (
            ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_annotations_error_component import (
            ApiV1EndpointsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_archived_at_error_component import (
            ApiV1EndpointsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_archived_by_error_component import (
            ApiV1EndpointsReconcileCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_archived_error_component import (
            ApiV1EndpointsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_archived_reason_error_component import (
            ApiV1EndpointsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_check_result_retention_days_error_component import (
            ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_check_results_error_component import (
            ApiV1EndpointsReconcileCreateCheckResultsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_created_by_component_error_component import (
            ApiV1EndpointsReconcileCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_created_by_user_error_component import (
            ApiV1EndpointsReconcileCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_criticality_error_component import (
            ApiV1EndpointsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_debug_mode_error_component import (
            ApiV1EndpointsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_discovery_enabled_error_component import (
            ApiV1EndpointsReconcileCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_display_name_error_component import (
            ApiV1EndpointsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_do_not_monitor_error_component import (
            ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_k8s_app_error_component import (
            ApiV1EndpointsReconcileCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_k8s_cluster_error_component import (
            ApiV1EndpointsReconcileCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_kind_error_component import (
            ApiV1EndpointsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_labels_error_component import (
            ApiV1EndpointsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_last_agent_metrics_error_component import (
            ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsReconcileCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_managed_by_content_type_error_component import (
            ApiV1EndpointsReconcileCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_managed_by_object_id_error_component import (
            ApiV1EndpointsReconcileCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_modified_by_user_error_component import (
            ApiV1EndpointsReconcileCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_name_error_component import (
            ApiV1EndpointsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_non_field_errors_error_component import (
            ApiV1EndpointsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_organization_id_error_component import (
            ApiV1EndpointsReconcileCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_platform_dns_record_created_error_component import (
            ApiV1EndpointsReconcileCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_platform_service_error_component import (
            ApiV1EndpointsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_pop_endpoint_error_component import (
            ApiV1EndpointsReconcileCreatePopEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_provider_error_component import (
            ApiV1EndpointsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_provider_id_error_component import (
            ApiV1EndpointsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_provider_reference_error_component import (
            ApiV1EndpointsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_region_error_component import (
            ApiV1EndpointsReconcileCreateRegionErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_remote_address_error_component import (
            ApiV1EndpointsReconcileCreateRemoteAddressErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_remote_port_error_component import (
            ApiV1EndpointsReconcileCreateRemotePortErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_resolved_ip_error_component import (
            ApiV1EndpointsReconcileCreateResolvedIpErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_s3_cluster_error_component import (
            ApiV1EndpointsReconcileCreateS3ClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_scope_error_component import (
            ApiV1EndpointsReconcileCreateScopeErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_sla_availability_error_component import (
            ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_sla_target_error_component import (
            ApiV1EndpointsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_sla_window_days_error_component import (
            ApiV1EndpointsReconcileCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_slo_availability_error_component import (
            ApiV1EndpointsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_slo_target_error_component import (
            ApiV1EndpointsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_slo_window_days_error_component import (
            ApiV1EndpointsReconcileCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_spec_error_component import (
            ApiV1EndpointsReconcileCreateSpecErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_target_availability_error_component import (
            ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_workspace_id_error_component import (
            ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1EndpointsReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateSpecErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1EndpointsReconcileCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateRemoteAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateRemotePortErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateCheckResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreatePopEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateResolvedIpErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateS3ClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1EndpointsReconcileCreateRegionErrorComponent):
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
        from ..models.api_v1_endpoints_reconcile_create_actual_availability_error_component import (
            ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_annotations_error_component import (
            ApiV1EndpointsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_archived_at_error_component import (
            ApiV1EndpointsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_archived_by_error_component import (
            ApiV1EndpointsReconcileCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_archived_error_component import (
            ApiV1EndpointsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_archived_reason_error_component import (
            ApiV1EndpointsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_check_result_retention_days_error_component import (
            ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_check_results_error_component import (
            ApiV1EndpointsReconcileCreateCheckResultsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_created_by_component_error_component import (
            ApiV1EndpointsReconcileCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_created_by_user_error_component import (
            ApiV1EndpointsReconcileCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_criticality_error_component import (
            ApiV1EndpointsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_debug_mode_error_component import (
            ApiV1EndpointsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_discovery_enabled_error_component import (
            ApiV1EndpointsReconcileCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_display_name_error_component import (
            ApiV1EndpointsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_do_not_monitor_error_component import (
            ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_k8s_app_error_component import (
            ApiV1EndpointsReconcileCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_k8s_cluster_error_component import (
            ApiV1EndpointsReconcileCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_kind_error_component import (
            ApiV1EndpointsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_labels_error_component import (
            ApiV1EndpointsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_last_agent_metrics_error_component import (
            ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1EndpointsReconcileCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_loadbalancer_instance_error_component import (
            ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_managed_by_content_type_error_component import (
            ApiV1EndpointsReconcileCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_managed_by_object_id_error_component import (
            ApiV1EndpointsReconcileCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_max_agents_per_endpoint_error_component import (
            ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_modified_by_user_error_component import (
            ApiV1EndpointsReconcileCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_name_error_component import (
            ApiV1EndpointsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_non_field_errors_error_component import (
            ApiV1EndpointsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_organization_id_error_component import (
            ApiV1EndpointsReconcileCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_platform_dns_record_created_error_component import (
            ApiV1EndpointsReconcileCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_platform_service_error_component import (
            ApiV1EndpointsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_pop_endpoint_error_component import (
            ApiV1EndpointsReconcileCreatePopEndpointErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_provider_error_component import (
            ApiV1EndpointsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_provider_id_error_component import (
            ApiV1EndpointsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_provider_reference_error_component import (
            ApiV1EndpointsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_region_error_component import (
            ApiV1EndpointsReconcileCreateRegionErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_remote_address_error_component import (
            ApiV1EndpointsReconcileCreateRemoteAddressErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_remote_port_error_component import (
            ApiV1EndpointsReconcileCreateRemotePortErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_resolved_ip_error_component import (
            ApiV1EndpointsReconcileCreateResolvedIpErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_s3_cluster_error_component import (
            ApiV1EndpointsReconcileCreateS3ClusterErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_scope_error_component import (
            ApiV1EndpointsReconcileCreateScopeErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_sla_availability_error_component import (
            ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_sla_target_error_component import (
            ApiV1EndpointsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_sla_window_days_error_component import (
            ApiV1EndpointsReconcileCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_slo_availability_error_component import (
            ApiV1EndpointsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_slo_target_error_component import (
            ApiV1EndpointsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_slo_window_days_error_component import (
            ApiV1EndpointsReconcileCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_spec_error_component import (
            ApiV1EndpointsReconcileCreateSpecErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_target_availability_error_component import (
            ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_endpoints_reconcile_create_workspace_id_error_component import (
            ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponent
                | ApiV1EndpointsReconcileCreateAnnotationsErrorComponent
                | ApiV1EndpointsReconcileCreateArchivedAtErrorComponent
                | ApiV1EndpointsReconcileCreateArchivedByErrorComponent
                | ApiV1EndpointsReconcileCreateArchivedErrorComponent
                | ApiV1EndpointsReconcileCreateArchivedReasonErrorComponent
                | ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponent
                | ApiV1EndpointsReconcileCreateCheckResultsErrorComponent
                | ApiV1EndpointsReconcileCreateCreatedByComponentErrorComponent
                | ApiV1EndpointsReconcileCreateCreatedByUserErrorComponent
                | ApiV1EndpointsReconcileCreateCriticalityErrorComponent
                | ApiV1EndpointsReconcileCreateDebugModeErrorComponent
                | ApiV1EndpointsReconcileCreateDiscoveryEnabledErrorComponent
                | ApiV1EndpointsReconcileCreateDisplayNameErrorComponent
                | ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponent
                | ApiV1EndpointsReconcileCreateK8SAppErrorComponent
                | ApiV1EndpointsReconcileCreateK8SClusterErrorComponent
                | ApiV1EndpointsReconcileCreateKindErrorComponent
                | ApiV1EndpointsReconcileCreateLabelsErrorComponent
                | ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponent
                | ApiV1EndpointsReconcileCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponent
                | ApiV1EndpointsReconcileCreateManagedByContentTypeErrorComponent
                | ApiV1EndpointsReconcileCreateManagedByObjectIdErrorComponent
                | ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponent
                | ApiV1EndpointsReconcileCreateModifiedByUserErrorComponent
                | ApiV1EndpointsReconcileCreateNameErrorComponent
                | ApiV1EndpointsReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1EndpointsReconcileCreateOrganizationIdErrorComponent
                | ApiV1EndpointsReconcileCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1EndpointsReconcileCreatePlatformServiceErrorComponent
                | ApiV1EndpointsReconcileCreatePopEndpointErrorComponent
                | ApiV1EndpointsReconcileCreateProviderErrorComponent
                | ApiV1EndpointsReconcileCreateProviderIdErrorComponent
                | ApiV1EndpointsReconcileCreateProviderReferenceErrorComponent
                | ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1EndpointsReconcileCreateRegionErrorComponent
                | ApiV1EndpointsReconcileCreateRemoteAddressErrorComponent
                | ApiV1EndpointsReconcileCreateRemotePortErrorComponent
                | ApiV1EndpointsReconcileCreateResolvedIpErrorComponent
                | ApiV1EndpointsReconcileCreateS3ClusterErrorComponent
                | ApiV1EndpointsReconcileCreateScopeErrorComponent
                | ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1EndpointsReconcileCreateSlaTargetErrorComponent
                | ApiV1EndpointsReconcileCreateSlaWindowDaysErrorComponent
                | ApiV1EndpointsReconcileCreateSloAvailabilityErrorComponent
                | ApiV1EndpointsReconcileCreateSloTargetErrorComponent
                | ApiV1EndpointsReconcileCreateSloWindowDaysErrorComponent
                | ApiV1EndpointsReconcileCreateSpecErrorComponent
                | ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_0 = (
                        ApiV1EndpointsReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_1 = (
                        ApiV1EndpointsReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_2 = (
                        ApiV1EndpointsReconcileCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_3 = (
                        ApiV1EndpointsReconcileCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_4 = (
                        ApiV1EndpointsReconcileCreateSpecErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_5 = (
                        ApiV1EndpointsReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_6 = (
                        ApiV1EndpointsReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_7 = (
                        ApiV1EndpointsReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_8 = (
                        ApiV1EndpointsReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_9 = (
                        ApiV1EndpointsReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_10 = (
                        ApiV1EndpointsReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_11 = (
                        ApiV1EndpointsReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_12 = (
                        ApiV1EndpointsReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_13 = (
                        ApiV1EndpointsReconcileCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_14 = (
                        ApiV1EndpointsReconcileCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_15 = (
                        ApiV1EndpointsReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_16 = (
                        ApiV1EndpointsReconcileCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_17 = (
                        ApiV1EndpointsReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_18 = (
                        ApiV1EndpointsReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_19 = (
                        ApiV1EndpointsReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_20 = (
                        ApiV1EndpointsReconcileCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_21 = (
                        ApiV1EndpointsReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_22 = (
                        ApiV1EndpointsReconcileCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_23 = (
                        ApiV1EndpointsReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_24 = (
                        ApiV1EndpointsReconcileCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_25 = (
                        ApiV1EndpointsReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_26 = (
                        ApiV1EndpointsReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_27 = (
                        ApiV1EndpointsReconcileCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_28 = (
                        ApiV1EndpointsReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_29 = (
                        ApiV1EndpointsReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_30 = (
                        ApiV1EndpointsReconcileCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_31 = (
                        ApiV1EndpointsReconcileCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_32 = (
                        ApiV1EndpointsReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_33 = (
                        ApiV1EndpointsReconcileCreateRemoteAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_34 = (
                        ApiV1EndpointsReconcileCreateRemotePortErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_35 = (
                        ApiV1EndpointsReconcileCreateCheckResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_36 = (
                        ApiV1EndpointsReconcileCreateDoNotMonitorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_37 = (
                        ApiV1EndpointsReconcileCreatePopEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_38 = (
                        ApiV1EndpointsReconcileCreateLastAgentMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_39 = (
                        ApiV1EndpointsReconcileCreateResolvedIpErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_40 = (
                        ApiV1EndpointsReconcileCreateMaxAgentsPerEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_41 = (
                        ApiV1EndpointsReconcileCreateCheckResultRetentionDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_42 = (
                        ApiV1EndpointsReconcileCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_43 = (
                        ApiV1EndpointsReconcileCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_44 = (
                        ApiV1EndpointsReconcileCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_45 = (
                        ApiV1EndpointsReconcileCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_46 = (
                        ApiV1EndpointsReconcileCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_47 = (
                        ApiV1EndpointsReconcileCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_48 = (
                        ApiV1EndpointsReconcileCreateS3ClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_endpoints_reconcile_create_error_type_49 = (
                        ApiV1EndpointsReconcileCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_endpoints_reconcile_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_endpoints_reconcile_create_error_type_50 = (
                    ApiV1EndpointsReconcileCreateLoadbalancerInstanceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_endpoints_reconcile_create_error_type_50

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_endpoints_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_endpoints_reconcile_create_validation_error.additional_properties = d
        return api_v1_endpoints_reconcile_create_validation_error

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
